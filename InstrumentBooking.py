# -*- coding: UTF-8 -*-
import re
import requests
import base64
import sys
import pytesseract
from PIL import Image
import http.cookiejar as cookielib
import urllib.request as urllib2
import time

task_attribute = {}


def main():
	return 0

def booking(value_instrument, value_year, value_month, value_day, value_start_time, value_stop_time, cycle_times = -1):
	#下面是参数，cycle_times是尝试预约次数，-1为无限次数；instrument_name是预约仪器
	instrument_name = "BD FACS CantoII流式细胞分析仪"
	session = requests.Session()
	session = sign_in(session)
	session1 = requests.Session()
	book_result = booking_with_para(session, value_instrument, value_year, value_month, value_day, value_start_time, value_stop_time, cycle_times)
	if book_result == "操作成功":
		print("预约成功！")
	else:
		print("循环次数结束，请重试")


def get_captcha(session):
	CaptchaUrl = "http://10.1.7.222/yqgl/admin/CreateImage.aspx"
	PostUrl = "http://10.1.7.222/yqgl/admin/default_yiqi.aspx"
	cookie = session.cookies
	# 验证码地址和post地址
	handler = urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(handler)
	# 将cookies绑定到一个opener cookie由cookielib自动管理
	username = 'wenyuqi'
	password = 'wenyuqi'
	# 用户名和密码
	picture = opener.open(CaptchaUrl).read()
	# 用openr访问验证码地址,获取cookie
	captcha_img = 'C:/Users/zhou lab/CbiCrawler/code/pic/verpic.jpg'
	local = open(captcha_img, 'wb')
	local.write(picture)
	local.close()
	# 保存验证码到本地
	image = Image.open(captcha_img)
	image = image.convert('RGB')
	captcha_code = pytesseract.image_to_string(image)
	print('Captcha is: ' + captcha_code)
	return session, captcha_code


def sign_in(session):
	url_login = "http://10.1.7.222/yqgl/admin/default_yiqi.aspx"
	
	session, captcha_code = get_captcha(session)
	payload_login = {
		'__VIEWSTATE':'/wEPDwUKMTAwMTQzNjkzOA9kFgICAw9kFgICDA8PFgQeBFRleHRlHgdWaXNpYmxlZ2RkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQJtMQUCbTMFAm0yoNlCc2s5wYvDBhhiVwwEnaav4EI=',
		'ename_b':'wenyuqi',
		'passwd_b':'wenyuqi',
		'textfield22':captcha_code,
		'm3.x':'44',
		'm3.y':'9',
		'__EVENTVALIDATION':'/wEWBwLhgKrNBwLz0qj1AgLD7+btDAKjoJjWDgL05LV6AsPv3u0MAsPv4u0M4lE30b6qW9ssE2cVwpbCDB0voDI=',
	}

	headers_login = {}

	contain = session.post(url_login, payload_login, headers_login)
	gb_contain = contain.content.decode("gb2312","ignore")
	if '<script language=Javascript>alert' in gb_contain:
		print('There is a mistake during signing in.\n Trying again...\n')
		time.sleep(2)
		sign_in(session)
	return session


def booking_with_para(session, value_instrument, value_year, value_month, value_day, value_start_time, value_stop_time, cycle_times = -1):
	status = 'cycle'
	instrument_id = {
		'BD FACS CantoII流式细胞分析仪':'20130403A0001',
		'BD Influx流式细胞分选仪':'20111229A0004',
		'BD LSRFortessa流式细胞分析仪':'20140416A0001',
		'BD LSRII数字化分析型流式细胞仪':'20111229A0001',
		'latest BD FACS AriaIII流式细胞分选仪':'20181108A0001',
		'new BD FACS AriaIII流式细胞分选仪':'20150506A0001',
		'old BD FACS AriaIII流式细胞分选仪':'20111229A0003',
		'Bioruptor plus超声破碎仪':'20150715A0001'
	}
	url_book = "http://10.1.7.222/yqgl/admin/apparatus/add4.aspx?id=" + instrument_id[value_instrument]
	contain = session.get(url_book)
	gb_contain = contain.content.decode("gb2312","ignore")
	EVENTVALIDATION_value = gb_contain.split('<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="')[1]\
		.split('" />')[0]
	VIEWSTATE_value = gb_contain.split('<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="')[1]\
		.split('" />')[0]
	payload_book = {
		'__EVENTTARGET':'',
		'__EVENTARGUMENT':'',
		'__LASTFOCUS':'',
		'__VIEWSTATE':VIEWSTATE_value,
		'apparatus_date_id_b':instrument_id[value_instrument] + '#' + value_year + '-' + value_month + '-' + value_day,
		'hour1_b':value_start_time,
		'hour2_b': value_stop_time,
		'teac_name_b':'1',
		'title1_b':'1',
		'title2_b':'1',
		'basic_money_sort_id_b':'1',
		'title3_b':'1',
		'apparatus_date_use1_id_b':'0001',
		'apparatus_date_use2_id_b':'0001',
		'miaoshu1_b':'1',
		'miaoshu2_b':'1',
		'Button1':'(unable to decode value)',
		'__EVENTVALIDATION':EVENTVALIDATION_value,
	}
	headers_book = {}

	contain = session.post(url_book, payload_book, headers_book)
	gb_contain = contain.content.decode("gb2312","ignore")
	try:
		book_result = gb_contain.split("<script language=Javascript>alert('")[1]\
			.split("');")[0]
	except:
		book_result = '未到时间'
	print('result is: ' + book_result + '\n')
	if cycle_times != -1:
		cycle_times -= 1
	if book_result != "操作成功" and cycle_times != 0:
		booking_with_para(session, value_instrument, value_year, value_month, value_day, value_start_time, value_stop_time, cycle_times)
	return session, book_result


if __name__ == '__main__':
	main()


# -*- coding: UTF-8 -*-
import re
import requests
#from skimage import io
import base64
import sys
#import tesserocr
from PIL import Image
import http.cookiejar as cookielib
import urllib.request as urllib2

task_attribute = {}


def main():
	session = requests.Session()
	session = sign_in(session)


def sign_in(session):
	url_login = "http://10.1.7.222/yqgl/admin/default_yiqi.aspx"
	#print(sys.getdefaultencoding())

	payload_login = {
		'__VIEWSTATE':'/wEPDwUKMTAwMTQzNjkzOA9kFgICAw9kFgICDA8PFgQeBFRleHRlHgdWaXNpYmxlZ2RkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQJtMQUCbTMFAm0yoNlCc2s5wYvDBhhiVwwEnaav4EI=',
		'ename_b':'1',
		'passwd_b':'1',
		'textfield22':'8774',
		'm3.x':'44',
		'm3.y':'9',
		'__EVENTVALIDATION':'/wEWBwLhgKrNBwLz0qj1AgLD7+btDAKjoJjWDgL05LV6AsPv3u0MAsPv4u0M4lE30b6qW9ssE2cVwpbCDB0voDI=',
	}

	headers_login = {}

	contain = session.post(url_login, payload_login, headers_login)
	print(str(contain.content).replace('\\r\\n', '\n'))
	a = contain.content.decode("gb2312","ignore")
	print(a)
	captcha_url = a.split('<img id="captcha_image" src="')[1]\
		.split('" alt="captcha" class="captcha_image"/>')[0]
	print(captcha_url)
	#image = io.imread(captcha_url)
	#io.imshow(image)
	#io.show()
	#parse_capt(captcha_url)
	return session


def parse_capt(image_url):
	# 获取这个图片的内容
	response = requests.get(image_url)

	# 获取base64的str
	base64_str = base64.b64encode(response.content)
	v_type = 'cn'
	# post提交打码平台的数据
	form = {
		'v_pic': base64_str,
		'v_type': v_type,
	}
	# 打码平台 Authorization的header
	headers = {
		'Authorization': 'APPCODE 926e3a416dd34ef0be35a19809ade4c9',
	}
	# 从打码平台获取验证码信息
	dmpt_url = 'http://yzmplus.market.alicloudapi.com/fzyzm'
	response = requests.post(dmpt_url, form, headers=headers)
	print(response.text)
	# captcha_value 就是我们的验证码信息
	captcha_value = response.json()['v_code']
	print(captcha_value)


if __name__ == '__main__':
	main()


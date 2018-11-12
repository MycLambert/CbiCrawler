#import urllib2
import http.cookiejar as cookielib
#import urllib
import urllib.request as urllib2
import re
import requests
'''模拟登录'''
# 防止中文报错
CaptchaUrl = "http://10.1.7.222/yqgl/admin/CreateImage.aspx"
PostUrl = "http://10.1.7.222/yqgl/admin/default_yiqi.aspx"
session = requests.session()
cookie = session.cookies
# 验证码地址和post地址
#cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
# 将cookies绑定到一个opener cookie由cookielib自动管理
username = 'wenyuqi'
password = 'wenyuqi'
# 用户名和密码
picture = opener.open(CaptchaUrl).read()
# 用openr访问验证码地址,获取cookie
local = open('C:/Users/zhou lab/CbiCrawler/code/pic/verpic.jpg', 'wb')
local.write(picture)
local.close()
# 保存验证码到本地
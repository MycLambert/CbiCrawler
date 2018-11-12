import re
import requests
#from bs4 import BeautifulSoup

task_attribute = {}

def getLogInContent(url_contain):
	headers = {
		'Cache-Control': "no-cache",
		'Postman-Token': "32188911-feff-41b4-a881-9382bd74ed76"
	}
	response = requests.request("GET", url_contain, headers=headers)
	contain = response.text
	return contain
	
def logIn():
	LogInContent = getLogInContent("http://10.1.7.222/yqgl/admin/default_yiqi.aspx")
	print(LogInContent + 'lalala\n')
	verCode = LogInContent.split('<tr><td width="100" height="35" align="center" ><input type="image" name="m3" id="m3" src="')[1].split('" onclick="javascript:WebForm_DoPostBackWithOptions')[0]
	print(verCode)

def main():
	print("Hello, world")
	
	logIn()
	
	'''
	<tr><td width="100" height="35" align="center" ><input type="image" name="m3" id="m3" src="
	url_contain = 'http://pm25.in/shenzhen'
	headers = {
		'Cache-Control': "no-cache",
		'Postman-Token': "32188911-feff-41b4-a881-9382bd74ed76"
	}

	response = requests.request("GET", url_contain, headers=headers)
	contain = response.text
	pm_range = contain.split('<div class="caption">')[1].split('<div class="caption">')[0]\
		.split('<div class="value">')[1]
	pm_result = re.search('\d{1,}', pm_range)
	if pm_result:
		print("PM2.5: ", pm_result.group())
	'''
	print("Bye, world")
	return 0


if __name__ == '__main__':
	main()
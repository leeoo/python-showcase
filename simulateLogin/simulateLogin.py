# -*- coding: utf-8 -*-

import urllib.request
import http.cookiejar

hostUrl = 'http://www.v2ex.com'
# httpsHostUrl = 'http://www.v2ex.com'
loginActionUrl = hostUrl + '/signin'
loginData = {'u': 'leeoo', 'p': '123@byd'}

loginData = urllib.parse.urlencode(loginData)

loginData = loginData.encode('utf-8')


#cookie = http.cookiejar.CookieJar()
#保存cookie，为登录后访问其它页面做准备  
#cjhdr  =  urllib.request.HTTPCookieProcessor(cookie)               
#opener = urllib.request.build_opener(cjhdr)  
opener = urllib.request.build_opener()

response = urllib.request.urlopen(loginActionUrl, loginData)
if response.status != 200:
	exit()

html = response.read()

htmlFile = open('v2ex.html', 'w', encoding='utf-8')

htmlFile.write(html.decode('utf-8'))

print(html)
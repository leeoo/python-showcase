# -*- coding: utf-8 -*-

import urllib.request
import http.cookiejar

hostUrl = 'http://www.aqbz.org/'
# loginActionUrl = hostUrl + 'AB_Result_Go.asp'
loginActionUrl = hostUrl + 'ABXX/AB_Result_Go.asp'
# loginData = {'u': 'leeoo', 'Wsub': 'ab'}
# loginData = {'ab': 'MAB100404', 'Wsub': 'ab'}
# loginData = {'Submit4': '查询', 'ab': 'MAB100404', 'Wsub': 'ab', 'cname': '', 'qname': '', 'sheng': 'all', 'xh': ''}
loginData = {'ab': 'MAB100404', 'Wsub': 'ab', 'cname': '', 'qname': '', 'sheng': 'all', 'xh': ''}

loginData = urllib.parse.urlencode(loginData)

loginData = loginData.encode('utf-8')


cj = http.cookiejar.CookieJar()

handler = urllib.request.HTTPCookieProcessor(cj)

opener = urllib.request.build_opener(handler)

opener.open(hostUrl)

# response = opener.open('http://www.aqbz.org/ABXX/AB_Result_bh.asp?ab=MAB100404', loginData)
response = opener.open(loginActionUrl, loginData)


#cookie = http.cookiejar.CookieJar()
#保存cookie，为登录后访问其它页面做准备  
#cjhdr  =  urllib.request.HTTPCookieProcessor(cookie)               
#opener = urllib.request.build_opener(cjhdr)  
# opener = urllib.request.build_opener()

# response = urllib.request.urlopen(loginActionUrl, loginData)


if response.status != 200:
	exit()

html = response.read()

# htmlFile = open('aqbz.html', 'w', encoding='utf-8')

# htmlFile.write(html.decode('utf-8'))

htmlFile = open('aqbz.html', 'w', encoding='utf-8')

htmlFile.write(html.decode('gbk'))

# print(html)

print('Ok')


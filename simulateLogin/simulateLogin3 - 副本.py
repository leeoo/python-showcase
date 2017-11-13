#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#Filename:states_code.py
 
import urllib.request
 
class RedirctHandler(urllib.request.HTTPRedirectHandler):
    """docstring for RedirctHandler"""
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        pass
 
def getUnRedirectUrl(url,timeout=10):
    req = urllib.request.Request(url)
    debug_handler = urllib.request.HTTPHandler(debuglevel = 1)
    opener = urllib.request.build_opener(debug_handler, RedirctHandler)
 
    html = None
    response = None
    try:
        response = opener.open(url,timeout=timeout)
        html = response.read()
    except urllib.URLError as e:
        if hasattr(e, 'code'):
            error_info = e.code
        elif hasattr(e, 'reason'):
            error_info = e.reason
    finally:
        if response:
            response.close()
    if html:
        return html
    # else:
    #     return error_info
 
hostUrl = 'http://www.aqbz.org/'
# loginActionUrl = hostUrl + 'AB_Result_Go.asp'
loginActionUrl = hostUrl + 'ABXX/AB_Result_Go.asp'

html = getUnRedirectUrl(loginActionUrl)
print(html)
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import sys

class zhihu(object):
    def __init__(self,email,password):
        self.email=email
        self.password=password
        self.myfqlink=[]

    def login(self):
        url="http://www.zhihu.com"
        login_url = url+'/login/email'
        login_data =   {'email':self.email,
                        'password':self.password,
                        'remember_me':'true',
                        'captcha':'',
                        '_xsrf':''}
        headers_base = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate, sdch',
                        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
                        'Connection': 'keep-alive',
                        'Host': 'www.zhihu.com',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
                        'Referer': 'http://www.zhihu.com/'}
        s = requests.session()
        def get_xsrf(url=None):
            r = s.get(url,headers=headers_base)
            xsrf = re.search(r'(?<=name="_xsrf" value=")[^"]*(?="/>)', r.text)
            if xsrf == None:
                return ''
            else:
                return xsrf.group(0)
        xsrf = get_xsrf(url)
        login_data['_xsrf'] = xsrf.encode('utf-8')
        captcha_url='http://www.zhihu.com/captcha.gif?type=login'
        captcha=s.get(captcha_url,stream=True)
        print captcha
        f = open('captcha.gif','wb')
        for line in captcha.iter_content(10):
            f.write(line)
        f.close()
        print u'输入验证码'
        captcha_str=raw_input()
        login_data['captcha']= captcha_str
        s.post(login_url,headers=headers_base,data=login_data)
        self.s=s


    def getqlinks(self):
        fq_url="https://www.zhihu.com/question/following"
        res= self.s.get(fq_url)
        q_link_list=re.findall(r'(?<=<a class=\"question_link\" target=\"_blank" href=\").*(?=\">)',res.text)
        self.myfqlink=q_link_list


    def get_oneqans(self,q_link):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        q_realink="https://www.zhihu.com"+q_link
        q_page=self.s.get(q_realink)
        html_page=BeautifulSoup(q_page.text)
        q_title=html_page.find('h2','zm-item-title zm-editable-content').get_text().strip()
        f = open(q_title+'.txt','w')
        q_detail=html_page.find('div', 'zm-editable-content').get_text()
        q_detail=(re.sub('<>','',q_detail)).strip()
        f.write('问题详情：'+q_title+'\n')
        f.write('问题细节：'+q_detail+'\n\n')
        q_ansnum=html_page.h3['data-num']
        if q_ansnum==0:
            print "no answer !"
        else :
           a_list_link=html_page.find_all('div','zm-item-answer')
           for a in a_list_link:
               a_text= str(a.find('div', 'zm-editable-content clearfix'))
               br=re.compile(r'<br/?>')
               others=re.compile(r'<[^>]+>')
               a_text=re.sub(br,'',a_text).strip()
               a_text=re.sub(others,'',a_text).strip()
               f.write('一条答案：'+a_text+'\n\n\n')
        f.close()

    def start_clawr(self):
        self.login()
        self.getqlinks()
        for q_link in self.myfqlink:
            self.get_oneqans(q_link)


if __name__=="__main__":
     print u'先输入邮箱'
     email=raw_input()
     print u'再输入密码'
     password=raw_input()
     one = zhihu(email,password)
     one.start_clawr()
     print u'爬完了，可以打开看了'



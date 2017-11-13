# zhouxianglh 2013.05.09 python3.3  
# Python 模拟登录,然后记录cookie,打卡签到  
import urllib.request  
import http.cookiejar  
import json  
import sys  
  
# 登录金山快盘  
params = {'ab': 'MAB100404', 'Wsub': 'ab', 'cname': '', 'qname': '', 'sheng': 'all', 'xh': ''}
webCookie = http.cookiejar.CookieJar()  
openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(webCookie))  
# 登录首页获取相关cookie用于登录  
webRequest = openner.open('http://www.aqbz.org/')    
# 登录快盘  
# webRequest = openner.open('http://www.aqbz.org/AB_Result_Go.asp', urllib.parse.urlencode(params).encode())    
webRequest = openner.open('http://www.aqbz.org/ABXX/AB_Result_bh.asp?ab=MAB100404')    
# 网页是用utf-8编码,所以这里用utf-8编码  
htmlData = webRequest.read().decode('gbk')    

print(htmlData)

# 解析json信息  
# result = json.loads(htmlData)   
# print("登录信息:", result["errcode"])  
  
  
# if result["state"] == "1" :  
#     print("登录成功,开始的卡")  
#     webRequest = openner.open("http://www.kuaipan.cn/index.php?ac=common&op=usersign")   
#     htmlData = webRequest.read().decode('utf-8')  
#     result = json.loads(htmlData)  
#     if result["state"] == -102:    
#         print("今天已签到过")  
#     elif result["state"] == 1:  
#         print("签到成功,赠送积分 %s,当前积分 %s,签到送空间 %sMB" % (result["increase"], result["status"]["points"], result["rewardsize"]))  
# else :  
#     print("登录失败")         
#     sys.exit()   
          
# 显示当肖快盘信息  
# webRequest = openner.open("http://www.kuaipan.cn/index.php?ac=home&op=space")   
# htmlData = webRequest.read().decode('utf-8')  
# result = json.loads(htmlData)  
# transform = 1024 * 1024 * 1024  # 以Byte为单位,所以这里要转换  
# print("当前空间:%.2f GB,已使用:%.2f GB" % (int(result["xLive"]["total"]) / transform, int(result["xLive"]["used"]) / transform))  
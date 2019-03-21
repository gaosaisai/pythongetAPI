#coding:utf-8
import urllib
import urllib.parse
import urllib.request

url = "http://reg.haibian.com/login/ajax_login"
# 定义请求数据，并且对数据进行赋值
data = {}
data['loginname'] = 'student08@qq.com'
data['password'] = '111111'
# 对请求数据进行编码
data = urllib.parse.urlencode(data)
# 将数据和URL进行连接
request = url+'?'+data
# 打开请求，获取对象
requestResponse = urllib.request.urlopen(request)
# 读取服务端返回的数据
ResponseStr = requestResponse.read()
# 打印数据
ResponseStr = ResponseStr.decode("unicode_escape")
print(requestResponse)
print (ResponseStr)
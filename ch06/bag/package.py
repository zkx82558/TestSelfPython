a=1

'''python中的常用模块'''
import sys
import time
import urllib.request
print((sys.getsizeof(28))) #判断字节
print(time.time())
print(time.localtime(time.time()))

print(urllib.request.urlopen('http://www.baidu.com').read())
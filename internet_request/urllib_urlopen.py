#-*-coding:utf-8-*- 
__author__ = 'Administrator'
from urllib import request

resp = request.urlopen('http://www.baidu.com')

print(resp.read())

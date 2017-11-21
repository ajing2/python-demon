#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/22 16:58
# @Author  : lingxiangxiang
# @File    : demon_json.py

# json四种方法：
# json.loads
# json.dumps
# 多s的就是来处理字符串的，没有多s的就是来处理文件的
# json.load
# json.dump

# loads    单词的意思是：加载    就是把json转换成其他格式，字符串或者文件相关的
# dumps    单词的意识是：颠倒    就是把其他对象或者格式，转换成json格式

# 例子1：  把python的dict格式转换成json字符串格式
import json
import urllib2
import chardet
import sys
print(sys.getdefaultencoding())
reload(sys)
sys.setdefaultencoding('utf8')
print(sys.getdefaultencoding())
a = dict(name='lingxiangxiang', age=25, message='you are so cool')
print(a)
print(type(a))
b = json.dumps(a)
print(b)
print(type(b))
print('1111111111111111')

# 例子2：
b = '\n{"a":1\n, "b":2, "name": "lingxiangxiang"}\n'
c = json.loads(b)
print(type(c))
print(c)
print(c['name'])


# 文件和json直接的转换


# 文件相关的话
# load 肯定是从文件中搞出来json数据，load肯定是把文件转换成json数据
# dump 就是把json数据写入到文件中
# 把json写入文件中   dump
jsondata = '''{"a": 1, "b": 2, "c": 3}'''
with open('a.txt', 'w') as f:
    json.dump(jsondata, f)

with open('a.txt', 'r') as fr:
    m = json.load(fr)
    print(m)
    print(type(m))


url = 'http://qwd.jd.com/fcgi-bin/qwd_searchitem_ex?g_tk=971960084&skuid=10657305771%7C11203636763%7C10571390914%7C13109264362%7C10386721898%7C12140975201%7C10439177256%7C13612561077%7C10171375206%7C13160174542%7C11641043874%7C13160308174%7C13618848172%7C13521003503%7C11062203238%7C10417123209%7C11712536222%7C12977266053%7C11287630528%7C11794389616'
req = urllib2.Request(url)
res = urllib2.urlopen(req)
result = res.read()
print(result)
print(chardet.detect(result))
m = json.loads(result)
print(type(m))
print(m)
print(json.dumps(m, ensure_ascii=False))
mmm = json.dumps(m, ensure_ascii=False)
print(type(mmm))
print(mmm)


# loads  dumps


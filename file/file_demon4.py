#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/30 15:56
# @Author  : lingxiangxiang
# @File    : file_demon4.py
import codecs

f = open('1.txt', 'rb')
# print(f.read())
f.close()

with codecs.open('1.txt', 'rb') as file:
    print(dir(file))
    # print(file.read())
    # print(file.closed)
# print(file.closed)
with codecs.open('1.txt', 'rb') as ff:
    for line, value in enumerate(ff):
        # print(line, value)
        if line == 4-1:
            print(value)
# cat 1.txt |grep aaa
# grep  正则
# re


import linecache
count = linecache.getline('1.txt', 4)
print(count)

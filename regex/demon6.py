#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/25 0:12
# @Author  : lingxiangxiang
# @File    : demon6.py

import re
prog = re.compile(r'(?P<tagname>abc)(\w*)(?P=tagname)')
result = prog.match('abclfjlad234sjldabc')

# finditer  迭代以后每个对象都是一个matche对象

print(dir(result))
print(result)

print(result.groups())
print(result.group(2))
print(result.group(1))
print('####'*10 + 'tagname'+ '###'*10)
print(result.group('tagname'))
# matche对象的group返回一个元祖，下标是以1开头


print(result.groupdict())

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/24 23:47
# @Author  : lingxiangxiang
# @File    : demon4.py


import re


p1 = re.compile(r'\d+')
a_str = 'one1two2three3four4'

# 正则对象的split方法，使用正则匹配进行分割字符串
# 最后以列表的形式返回回去
print(p1.split(a_str))

# 正则对象那个的findall方法，来查找符合对象的自字符串
# 最后是以列表的形式返回回去
print(p1.findall(a_str))

for i in p1.finditer(a_str):
    print(i.group())

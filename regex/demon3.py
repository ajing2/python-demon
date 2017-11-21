#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/24 23:31
# @Author  : lingxiangxiang
# @File    : demon3.py

# 正则对象的match匹配
import re
reg = re.compile(r'\w*((hello w.*)(hello l.*))')
print(dir(reg))
a = 'hello world hello ling'
result = reg.match(a)
print(result)
print(result.groups())

b = 'aa' + a
print(b)
result2 = reg.match(b)
print(result2)
print(result2.groups())


# 正则对象的search方法做一个比较
m = 'sadfjlasdjflsdajlf'
print('###'*30)
result3 = reg.search(b)
print(result3)
print(result3.groups())


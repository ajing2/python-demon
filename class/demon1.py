#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/13 21:49
# @Author  : lingxiangxiang
# @File    : demon1.py
class ren(object):
    '''this class is abort ren class'''
    name = 'meizi'
    sex = 'F'
    def hello(self):
        print('hello world!')

a = ren()
print(type(a))
print(a.name)
print(a.sex)
a.hello()
a.name = 'meinv'
print('#########################')
print(a.name)
print(dir(a))



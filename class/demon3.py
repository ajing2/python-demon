#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/13 22:28
# @Author  : lingxiangxiang
# @File    : demon3.py
class A(object):
    pass
class B(object):
    pass

class C(A, B):
    pass


class parent():
    name = 'parent'
    sex = 'F'
    def __init__(self):
        print('my name is {0}'.format(self.name))
    def get_name(self):
        return self.name
    def get_sex(self):
        return self.sex

class child(parent):
    name = 'child'
    # sex = 'M'
    def __init__(self):
        print('my name is {0}'.format(self.name))
    def hello(self):
        print('hello world')


a = child()
a.hello()
print(a.get_name())
print(a.get_sex())



#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/13 23:29
# @Author  : lingxiangxiang
# @File    : demon7.py

class A(object):
    '''hedasfasdlfasdfjalsdfjlasdjf'''
    _name = 'ling'
    __sex = 'F'
    def hello(self):
        print(self._name)
        print(self.__sex)
    def get_sex(self):
        return self.__sex

a = A()
print(a._name)
a.hello()
print(a.get_sex())
print(dir(a))

print(a.__doc__)
print(a.__class__)
print(a.__dict__)

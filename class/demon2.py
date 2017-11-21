#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/13 22:06
# @Author  : lingxiangxiang
# @File    : demon2.py
class ren():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def hello(self):
        print('hello {0}'.format(self.name))

test = ren('lingxiangxiang', 'M')

test.hello()

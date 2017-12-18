#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/13 22:45
# @Author  : lingxiangxiang
# @File    : demon4_test.py

class parent(object):
    parent_name = 'parent'
    sex = 'F'
    def __init__(self, address, age):
        self.address = address
        self.age = age
        print('my name is {0}'.format(self.parent_name))
    def get_name(self):
        print('parent parent parent parent####################################')
        return self.parent_name
    def get_sex(self):
        return self.sex

class child(parent):
    child_name = 'child'
    # sex = 'M'
    def __init__(self, address, age):
        super(child, self).__init__(address, age)
        # parent.__init__(self, address, age)
        print('my name is {0}'.format(self.child_name))
    def hello(self):
        print('hello world')
    def get_name(self):
        super(child, self).get_name()
        print('todaoy is nice day.')
        return 'hello $$$$$$$$$$$$$$$$$$$$$'


a = child('beijing', 10)
a.hello()
print(a.get_name())
print(a.get_sex())
print(a.address)
print(a.age)



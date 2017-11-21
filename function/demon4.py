#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/5 22:20
# @Author  : lingxiangxiang
# @File    : demon4.py

# 匿名函数：没有名字的函数
def sum(x, y):
    return x+y

m = lambda x, y: x+y
print(m)
print(m(4, 5))

# sorted()高阶函数
# 对字典进行排序
print('###########字典排序#################')
mm = dict(a=1, c=3, b=10, d=9)
print(mm)
for i in mm:
    print i
print('jjjjjjjjjjjj')
for j in mm.iteritems():
    print(j)
# print(dir(mm))
# help(sorted)
# test = sorted(mm)
test = sorted(mm.iteritems(), key=lambda d: d[1])
print(test)
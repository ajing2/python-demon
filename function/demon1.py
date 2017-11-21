#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/5 21:31
# @Author  : lingxiangxiang
# @File    : demon1.py
# 函数的定义
def sum(x, y):
    print('x = {0}'.format(x))
    print('y = {0}'.format(y))
    return x+y
m = sum(3, 10)
print(m)

# 函数的参数
# 1.给b变量设定一个默认的值
# 如果实参传入的时候，制定了b的值，那b优先选择传入的实参，当b没有值时，才会用默认值
def funcA(a, b=0):
  print a
  print b
funcA(1)
funcA(10, 20)




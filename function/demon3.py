#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/5 22:03
# @Author  : lingxiangxiang
# @File    : demon3.py

# map()函数，第一个参数为自定义函数，第二个参数为一个课迭代对象
lt = (1, 2, 3, 4, 5)
def f2(x):
    return x*x
ml = map(f2, lt)
print(type(ml))
print(ml)
# reduece函数
# 传入的函数必须接受两个参数，
# 把可迭代对象的前两个参数作为函数的实参，传入到f函数中
# 把每次f运算的结果作为第一个实参，可迭代对象的下一个元素作为另一个实参，传入函数f中，
# 以此类推,最终得到结果
print('###############reduce###########')
def f(x, y):
    return x + y
print(reduce(f, [1, 2, 3, 4, 5], 10))

# filter函数
#每次把可迭代对象的元素传入进去，如果返回为True，则保留该元素，如果返回为False, 则不保留该元素

a = [1, 2, 3, 4, 5, 6]
def is_odd(x):
    return x%2 == 1
print(filter(is_odd, a))
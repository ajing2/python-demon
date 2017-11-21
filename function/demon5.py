#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/5 22:49
# @Author  : lingxiangxiang
# @File    : demon7.py
# 列表生成式
li = [x*x  for x in xrange(1, 101) if x%2 == 0]
print(li)

def funa():
    a = []
    for x in xrange(1, 101):
        if x%2 ==0:
            a.append(x*x)
    return a
print(funa())
# range()   xrange()

# 2 4 6 8 10


# 列表生成器
# 1，最简单的办法：把原来的生成式的[]换成()就ok了
lt = (x*x for x in xrange(1, 11) if x%2 ==0)
print(lt)
print(type(lt))
for i in lt:
    print(i)
# 2, 函数中定义列表生成器
print('##########第二种方法##############')
def fib(n):
    sum = 0
    i = 0
    while(i<n):
        sum = sum +i
        i+=1
        yield(sum)
print(type(fib(10)))
for x in fib(10):
    print(x)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/5 22:02
# @Author  : lingxiangxiang
# @File    : demon2.py

# 2，参数为tuple
print('##########参数tuple###################')
def funcD(a, b, *c):
  print(a)
  print(b)
  print "length of c is: %d " % len(c)
  print(c)

funcD(1, 2, 3, 4, 5, 6)
test = ('hello', 'world')
funcD(1, 2, *test)
# main(m, *args)


print('##############参数字典################')
# 3.参数为dict
def funcF(a, **b):
  print(a)
  print(b)
  for x in b:
    print x + ": " + str(b[x])

funcF(100, x="hello", y='你好')
args = {'1': 'a', '2': 'b'}
funcF(100, **args)




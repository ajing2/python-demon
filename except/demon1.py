#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/25 14:49
# @Author  : lingxiangxiang
# @File    : demon1.py

try:
    a = 10
    b = 0
    a/b
except Exception as e:
    print(e)
    print('error')
    raise e
else:
    print('this is ok!')
finally:
    print('end')
print('hello world lingxinagxinag!')
# object   这个是所有类的基类
# Exception 这个类是所有异常类的基类

# a = [1, 2, 4]
# # try:
# print(a[4])
# except IndexError as e:
#     print(e)

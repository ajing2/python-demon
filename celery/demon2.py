#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/26 21:56
# @Author  : lingxiangxiang
# @File    : demon2.py
import time

from ajing import add

a = add.delay(10, 20)
print(a)
print(type(a))
time.sleep(1)
print(a.result)
print(a.status)
# print(a.get(timeout=3))
print(a.ready())
print(dir(a))
print(a.id)
print(a.task_id)


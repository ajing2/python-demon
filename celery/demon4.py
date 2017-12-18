#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 23:07
# @Author  : lingxiangxiang
# @File    : demon4_test.py
import time

from demon3 import *
r1 = taskA.delay(10, 20)
print(r1.result)
print(r1.status)
r2 = taskB.delay(1, 2, 3)
time.sleep(1)
print(r2.result)
print(r2.status)
# print(dir(r2))
r3 = add.delay(100, 200)
print(r3.result)
print(r3.status)
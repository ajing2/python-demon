#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/25 18:42
# @Author  : lingxiangxiang
# @File    : demon2.py
#
# Subclass relationships:   子类之间的对应关系
#
# object
#     timedelta
#     tzinfo
#     time
#     date
#         datetime
# time模块基本不用于取时间，取时间推荐使用datetime模块
# time独有的用法:
import time

for i in xrange(1, 10):
    print(i)
    time.sleep(0.1)


# datetime

from datetime import datetime, timedelta

now_time = datetime.now()
print(now_time)
new_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
a = now_time.strftime('%c')
print(new_time)
print(a)
# now 获得当前的时间，strftime用来表示显示时间的格式


# 如果我们要取昨天或者明天的日期，

print('########################')
now_time = datetime.now()
yesterday = now_time + timedelta(days=-1)
tomorrow_1 = now_time + timedelta(days=-1)
tomorrow = tomorrow_1.strftime('%Y-%m-%d')
print(yesterday)
print(tomorrow)
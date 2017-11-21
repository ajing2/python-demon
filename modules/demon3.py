#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/25 19:32
# @Author  : lingxiangxiang
# @File    : demon3.py
from datetime import datetime
import time

now_time = datetime.now()
print(now_time)
print(type(now_time))
print('########time to str################')
# _time = now_time.strftime('%Y-%m-%d %H:%M:%S')
_time = datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
print(_time)
print(type(_time))
print('########str to time################')
_d_time = datetime.strptime(_time, '%Y-%m-%d %H:%M:%S')
print(_d_time)
print(type(_d_time))



print('############时间戳  stamp############')
# 时间戳抓换成时间对象
_a = time.time()
print(_a)
_n_time = datetime.fromtimestamp(_a)
print(_n_time)
print(type(_n_time))

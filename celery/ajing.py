#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/26 21:51
# @Author  : lingxiangxiang
# @File    : ajing.py

from celery import Celery

broker = "redis://192.168.48.131:6379/5"
backend = "redis://192.168.48.131:6379/6"
app = Celery("ajing", broker=broker, backend=backend)

@app.task
def add(x, y):
    return x+y
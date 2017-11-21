#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/25 9:27
# @Author  : lingxiangxiang
# @File    : test.py
import codecs

with codecs.open("file.txt", "r") as f:
    # x = f.readlines()
    print(f.readlines())
    print(f.readlines())
    # print(x)
    # print(x[0])

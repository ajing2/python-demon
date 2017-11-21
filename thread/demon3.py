#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/5 21:55
# @Author  : lingxiangxiang
# @File    : demon3.py
import threading


def worker(l):
    l.append("ling")
    l.append("huo")
    l.append("wang")

if __name__ == "__main__":
    l = list()
    l += range(1, 10)
    print(l)
    t = threading.Thread(target=worker, args=(l,))
    t.start()
    print(l)

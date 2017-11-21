#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/2 21:42
# @Author  : lingxiangxiang
# @File    : demon6.py
import multiprocessing


def worker(d, l):
    l += range(11, 16)
    for i in xrange(1, 6):
        key = "key{0}".format(i)
        val = "val{0}".format(i)
        d[key] = val


if __name__ == "__main__":
    manager = multiprocessing.Manager()
    d = manager.dict()
    l = manager.list()
    p = multiprocessing.Process(target=worker, args=(d, l))
    p.start()
    p.join()
    print(d)
    print(l)
    print("main end")


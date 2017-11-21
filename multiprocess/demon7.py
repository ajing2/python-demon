#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/2 22:05
# @Author  : lingxiangxiang
# @File    : demon7.py
import multiprocessing

import time


def worker(msg):
    print("########start {0}##########".format(msg))
    time.sleep(1)
    print("########end   {0}##########".format(msg))

if __name__ == "__main__":
    print("main start")
    pool = multiprocessing.Pool(processes=3)
    for i in xrange(1, 10):
        msg = "hello {0}".format(i)
        pool.apply_async(func=worker, args=(msg,))
    pool.close()
    pool.join() #在join之前，一定要调用close，否则报错。
    print("main end")

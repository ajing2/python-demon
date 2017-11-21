#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/1 21:34
# @Author  : lingxiangxiang
# @File    : demon3.py
import multiprocessing
import time


def worker(name, interval):
    print("{0} start".format(name))
    time.sleep(interval)
    print("{0} end".format(name))

if __name__ == "__main__":
    print("main start")
    print("this Computer has {0}".format(multiprocessing.cpu_count()))
    p1 = multiprocessing.Process(target=worker, args=("worker1", 2))
    p2 = multiprocessing.Process(target=worker, args=("worker2", 3))
    p3 = multiprocessing.Process(target=worker, args=("worker3", 4))
    p1.start()
    p2.start()
    p3.start()
    for p in multiprocessing.active_children():
        print("the pid of {0} is {1}".format(p.name, p.pid))
    print("main end")
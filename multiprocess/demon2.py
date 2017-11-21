#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/1 21:12
# @Author  : lingxiangxiang
# @File    : demon2.py

import multiprocessing
# multiprocessing.active_children()    列出存在的子进程
# 1 ->2, 3, 4
#cpu_count()     统计cpu的个数
import time


def worker(interval):
    time.sleep(interval)
    print("hello world")

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker, args=(5,))
    p.start()
    print(p.is_alive())
    p.join(timeout=3)  #等待子进程执行完毕或者超时退出
    print("end main")
    print(p.name)
    print(p.pid)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/1 22:04
# @Author  : lingxiangxiang
# @File    : demon4.py
import multiprocessing

# lock = multiprocessing.Lock()
# lock.acquire()           获取锁
# lock.release()          释放锁
# with lock:
# 不加锁程序
# number   +1
# number   +3
import time


def add(number, value, lock):
    lock.acquire()
    try:
        print("init add{0} number = {1}".format(value, number))
        for i in xrange(1, 6):
            number += value
            time.sleep(1)
            print("add{0} number = {1}".format(value, number))
    except Exception as e:
        raise e
    finally:
        lock.release()

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    number = 0
    p1 = multiprocessing.Process(target=add, args=(number, 1, lock))
    p2 = multiprocessing.Process(target=add, args=(number, 3, lock))
    p1.start()
    p2.start()
    print("main end")

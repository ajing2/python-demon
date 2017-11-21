#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/1 22:04
# @Author  : lingxiangxiang
# @File    : demon4.py

import multiprocessing
import time


# Value()
# Array()

def add(number, add_value, lock):
    lock.acquire()
    try:
        print("init add{0} number = {1}".format(add_value, number.value))
        for i in xrange(1, 6):
            number.value += add_value
            print("##############add{0} has added!############".format(add_value))
            time.sleep(1)
            print("add{0} number = {1}".format(add_value, number.value))
    except Exception as e:
        raise e
    finally:
        lock.release()

def change(arr):
    for i in range(len(arr)):
        arr[i] = -arr[i]

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    number = multiprocessing.Value('i', 0)
    arr = multiprocessing.Array('i', range(10))
    print(arr[:])
    p1 = multiprocessing.Process(target=add, args=(number, 1, lock))
    p2 = multiprocessing.Process(target=add, args=(number, 3, lock))
    p3 = multiprocessing.Process(target=change, args=(arr,))
    p1.start()
    p2.start()
    p3.start()
    p3.join()
    print(arr[:])
    print("main end")

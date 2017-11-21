#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/2 23:29
# @Author  : lingxiangxiang
# @File    : demon1.py
import threading


def worker(n):
    print("start worker{0}".format(n))


class MyThread(threading.Thread):
    def __init__(self, args):
        super(MyThread, self).__init__()
        self.args = args
    def run(self):
        print("start MyThread{0}".format(self.args))

if __name__ == "__main__":
    for i in xrange(1, 6):
        t1 = threading.Thread(target=worker, args=(i,))
        t1.start()
    t1.join()

    for x in xrange(6, 11):
        t2 = MyThread(x)
        t2.start()
    t2.join()


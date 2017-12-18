#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/9 22:45
# @Author  : lingxiangxiang
# @File    : demon4_test.py
import datetime
import redis


def withpipe(r):
    pipe = r.pipeline(transaction=True)
    for i in xrange(1, 1000):
        key = "test1" + str(i)
        value = "test1" + str(i)
        pipe.set(key, value)
    pipe.execute()


def withoutpipe(r):
    # pipe = r.pipeline(transaction=True)
    for i in xrange(1, 1000):
        key = "test1" + str(i)
        value = "test1" + str(i)
        r.set(key, value)

if __name__ == "__main__":
    pool = redis.ConnectionPool(host="192.168.48.131", port=6379, db=0)
    r1 = redis.Redis(connection_pool=pool)
    r2 = redis.Redis(connection_pool=pool)
    start = datetime.datetime.now()
    print(start)
    withpipe(r1)
    end = datetime.datetime.now()
    # print((end-start).microseconds)
    print(end-start)
    t_time = (end - start).microseconds
    print("withpipe time is : {0}".format(t_time))

    start = datetime.datetime.now()
    withoutpipe(r2)
    end = datetime.datetime.now()
    t_time = (end - start).microseconds
    print("withoutpipe time is : {0}".format(t_time))







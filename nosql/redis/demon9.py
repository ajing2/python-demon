#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11 23:36
# @Author  : lingxiangxiang
# @File    : demon9.py



import redis

pool = redis.ConnectionPool(host="192.168.48.131", port=6379, db=0)
r = redis.Redis(connection_pool=pool)

r.delete("name1")
print(r.keys())
print(r.type("name"))
# r.rename("name", "name1")
print(r.exists("name"))
print(r.exists("name2"))
r.move("dict1", 1)



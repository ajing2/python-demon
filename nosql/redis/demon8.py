#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11 23:21
# @Author  : lingxiangxiang
# @File    : demon8.py


import redis

pool = redis.ConnectionPool(host="192.168.48.131", port=6379, db=0)
r = redis.Redis(connection_pool=pool)
# hash  类型的操作
# 就是一个name对应一个字典
# hset  hget   hmset   hmget
r.hset("dict1", "hello", "world")
print(r.hget("dict1", "hello"))
r.hmset("dict1", {"k1": "v1", "k2": "v2", "k3": "v3"})
print(r.hmget("dict1", "k1", "k2", "hello"))
print(r.hgetall("dict1"))

print(r.hlen("dict1"))
print(r.hkeys("dict1"))
print(r.hvals("dict1"))
print(r.hexists("dict1", "hello"))
print(r.hexists("dict1", "ling"))
r.hdel("dict1", "hello")
print(r.hgetall("dict1"))
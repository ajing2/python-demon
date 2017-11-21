#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/10 0:02
# @Author  : lingxiangxiang
# @File    : demon5.py

import redis

pool = redis.ConnectionPool(host="192.168.48.131", port=6379, db=0)
r = redis.Redis(connection_pool=pool)

r.set("name", "lingxiangxiang")
print(r.keys())
print(r.get("name"))
r.mset(name1 = "ling", name2 = "shang")
print(r.mget("name1", "name2"))
r.mset({"hello": "world", "nihao": "nice"})
print(r.keys())
print(r.mget("hello", "nihao"))

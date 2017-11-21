#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/9/17 23:54
# @Author  : lingxiangxiang
# @File    : demon2.py
import redis

pool = redis.ConnectionPool(host="192.168.48.128", port=6379, db=0)
r = redis.Redis(connection_pool=pool)
pipe = r.pipeline(transaction=True)
r.set("test5", "hello5")
r.set("test6", "hello6")
r.set("test7", "hello7")
r.set("test8", "hello8")
# pipe.execute()
# print(r.get("name"))
print(r.keys())
print(r.get("name"))
r.mset(name1="shang", name2="ling")
r.mset({"name3": "kong", "name4": "gu"})
print(r.mget("name1", "name2", "name3", "name4"))
r.lpush("list_name", 2)
r.lpush("list_name", 3, 4, 5)
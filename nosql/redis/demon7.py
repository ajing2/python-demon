#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/10 22:05
# @Author  : lingxiangxiang
# @File    : demon7.py


import redis

pool = redis.ConnectionPool(host="192.168.48.131", port=6379, db=0)
r = redis.Redis(connection_pool=pool)
# r.sadd(name, *args)   增加一个name对应的一个集合
r.sadd("set_name", "aa", "bb", "cc")
# smember   就是查看集合的所有元素
print(r.smembers("set_name"))
print(r.scard("set_name"))
# scard    等同于list  len    查看元素的个数
r.srem("set_name", "aa")
# srem(name, value)   删除值为value的指定集合中的某个元素
print(r.smembers("set_name"))
r.sadd("set_name1", "cc", "dd", "ee")
# sinter   两个集合的交集
print(r.sinter("set_name", "set_name1"))
# sunion      两个集合的并集
print(r.sunion("set_name", "set_name1"))

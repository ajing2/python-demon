#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/10 21:20
# @Author  : lingxiangxiang
# @File    : demon6.py


import redis

pool = redis.ConnectionPool(host="192.168.48.131", port=6379, db=0)
r = redis.Redis(connection_pool=pool)
# lpush  在list的左边增加一个元素           left
# rpush  在list的右边增加一个元素           right
r.lpush("list1", "test1")
r.rpush("list1", "ling")
r.lpush("list1", "test2")
r.lpush("list1", "test3")
r.lpush("list1", "test2")
r.lpush("list1", 2, 3, 4)
r.lpush("list1", "test2")
print(r.lrange("list1", 0, -1))

# 最终的list结果是    [4, 3, 2, "test3", "test2", "test1", "ling"]

# 在中间位置增加一个元素
# linsert(name,where,refvalue,value)
# name   代表的是list对应的key值
# where     AFTER   BEFORE
# refvalue    list中的某个元素
# value      你要增加的值是什么
r.linsert("list1", "AFTER",  "test2", "hello")
print(r.lrange("list1", 0, -1))
r.lset("list1", 2, "world")
# lset  更改某个元素的值
# r.lset(name,index,value)
print(r.lrange("list1", 0, -1))
print(r.lindex("list1", 2))
# lindex   查看list某个下标的值
print(r.lpop("list1"))
# lpop从list的最左边删除一个元素，返回删除元素的值
print(r.lrange("list1", 0, -1))
r.lrem("list1", "world")
# r.lrem(name,value,num):
# num，  num=0，删除列表中所有的指定值；
           # num=2,从前到后，删除2个；
           # num=-2,从后向前，删除2个

print(r.lrange("list1", 0, -1))



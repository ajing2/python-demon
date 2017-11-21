#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/15 0:08
# @Author  : lingxiangxiang
# @File    : demon13.py
import memcache

mc = memcache.Client(["192.168.48.131:11211"])

# set  set_multi(dict)
# get  get_multi(list)
# add
# replace
# delete   delete_multi

mc.set_multi({"test1":"v1", "test2": "v2", "test3": "v3", "test4": "v4"})
print(mc.get_multi(["test1", "test2", "test3", "test4"]))
mc.delete("test1")
mc.delete_multi(["test2", "test3", "test4"])
print(mc.get_multi(["test1", "test2", "test3", "test4"]))


# append 和prepend
# mc.prepend()
# mc.append()

mc.set_multi({"test1":"v1", "test2": "v2", "test3": "v3", "test4": "v4"})
mc.append("test1", "ling")
print(mc.get("test1"))
mc.prepend("test2", "hello")
print(mc.get("test2"))

# incr  默认自增1      第二个参数指定增加的数字为n
# decr   默认自减1     第二个参数制定减少的数据n


mc.set("shop", 1000)
mc.incr("shop")
print(mc.get("shop"))
mc.incr("shop", 100)
print(mc.get("shop"))

mc.decr("shop")
print(mc.get("shop"))
mc.decr("shop", 500)
print(mc.get("shop"))

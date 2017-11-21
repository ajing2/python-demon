#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/14 22:54
# @Author  : lingxiangxiang
# @File    : demon12.py
import memcache

mc = memcache.Client(["192.168.48.131:11211"], debug=True)
print(dir(mc))
# add(key, value)
# mc.add("k1", "v1")
# print(mc.get("k1"))
#
# # replace
# mc.replace("k1", "hello world")
# print(mc.get("k1"))

# set(key value)

mc.set("k2", "v2")
print(mc.get("k2"))

mc.set("k2", "hello2")
print(mc.get("k2"))

# set和add的区别
#set = add + repalce
# 如果这个key值存在，add就会报错， set不会报错，会进行重新赋值并覆盖

# set_multi(dict)    一次设置多个key:value
# get_multi(list)    一次获取到多个keys，每个key要以list的形式作为参数传入  返回类型为dict
# get(key)   获得该key对应的value的值
mc.set_multi({"k100": "v100", "k101": "v101", "k102": "v102"})
print(mc.get_multi(["k100", "k101", "k102"]))


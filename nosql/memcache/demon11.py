#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/14 22:21
# @Author  : lingxiangxiang
# @File    : demon11.py


# 安装memecache的客户端   pip install memcache

import memcache
# memcache.Client  初始化一个memcache的客户端对象
mc = memcache.Client([("192.168.48.131:11211", 1), ("192.168.48.131:11212", 2), ("192.168.48.131:11213", 1)], debug=True)
mc.set("k1", "v1")
print(mc.get("k1"))


mc1 = memcache.Client(["192.168.48.131:11213"], debug=True)
print(mc1.get("k1"))
mc1.set("k1", 88888)
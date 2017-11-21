#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/14 23:52
# @Author  : lingxiangxiang
# @File    : SDA.py

import memcache
import time

mc = memcache.Client(['192.168.48.131:11211'], debug=True)

mc.set("k1", 1000)
mc.gets("k1")
# mc.set("k1", 89080)
time.sleep(20)
print(mc.cas("k1", 999))
print(mc.get("k1"))
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/9/25 23:40
# @Author  : lingxiangxiang
# @File    : domon3.py
import redis


# redis的小试牛刀
r = redis.Redis(host="192.168.48.131", port=6379)
# r = redis.Redis(**redis_config)
r.set("ling", "you are so cool!")
r.set("shang", "I love you")
r.set("test1", "test1")
r.set("test2", "test2")
r.set("test3", "test3")
r.set("test4", "test4")
# # set 操作   第一参数是key， 第二个参数是value
print(r.keys())
# # r.keys   就是获取到所有的key
# print(r.get("ling"))
# # r.get    就是获到key的值


#
# # # redis链接池
# def get_redis_connect():
#     redis_config = {
#         "host": "192.168.48.131",
#         "port": 6379
#     }
#     pool = redis.ConnectionPool(**redis_config)
#     r = redis.Redis(connection_pool=pool)
#     return r
# if __name__ == "__main__":
#     r = get_redis_connect()
#     r.set("name", "lingxiangxinag")
#     r.set("hello", "world")
#     print(r.get("name"))
#     print(r.keys())
#     print(r.set("test", "the teacher of ling is very very cool!"))
#     print(r.get("test"))
#


# redis的管道，可以一次执行多条redis命令

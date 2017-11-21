#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/9/17 11:26
# @Author  : lingxiangxiang
# @File    : demon1.py
import MySQLdb

# 链接数据库，
# host   数据库ip
# port   数据库监听的端口
# user   链接数据库用户
# passwd   用户密码
# db     数据库名字
# charset  字符集   utf-8



# conn=MySQLdb.connect(host="192.168.48.128",user="xiang",passwd="123456",db="python",charset="utf8", port=3306)

def connect_mysql():
    db_config = {
        "host": "192.168.48.128",
        "port": 3306,
        "user": "xiang",
        "passwd": "123456",
        "db": "python",
        "charset": "utf-8"
    }
    try:
        cnx = MySQLdb.connect(**db_config)
    except Exception as e:
        raise e
    return cnx



print(connect_mysql())
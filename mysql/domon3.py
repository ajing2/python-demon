#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/9/18 22:17
# @Author  : lingxiangxiang
# @File    : domon3.py

from demon2 import connect_mysql


import MySQLdb


def connect_mysql():
    db_config = {
        "host": "192.168.48.128",
        "port": 3306,
        "user": "xiang",
        "passwd": "123456",
        "db": "python",
        "charset": "utf8"
    }
    try:
        cnx = MySQLdb.connect(**db_config)
    except Exception as e:
        raise e
    return cnx
if __name__ == "__main__":
    sql = "select * from tmp;"
    sql1 = "insert into tmp(id) value (%s);"
    param = []
    for i in xrange(100, 130):
        param.append([str(i)])
    print(param)
    cnx = connect_mysql()
    cus = cnx.cursor()
    print(dir(cus))
    try:
        cus.execute(sql)
        cus.executemany(sql1, param)
        # help(cus.executemany)
        result1 = cus.fetchone()
        print("result1")
        print(result1)

        result2 = cus.fetchmany(3)
        print("result2")
        print(result2)

        result3 = cus.fetchall()
        print("result3")
        print(result3)
        cus.close()
        cnx.commit()

    except Exception as e:
        cnx.rollback()
        raise e
    finally:
        cnx.close()



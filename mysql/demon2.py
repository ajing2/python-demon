#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/9/17 11:50
# @Author  : lingxiangxiang
# @File    : demon2.py
import MySQLdb


def connect_mysql():
    db_config = {
        "host": "192.168.48.131",
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
    cnx = connect_mysql()
    print(dir(cnx))
    print(cnx)
    cus = cnx.cursor()
    try:
        cus.execute(sql)
        cus.close()
        cnx.commit()
    except Exception as e:
        raise e
        cnx.rollback()
    finally:
        cnx.close()



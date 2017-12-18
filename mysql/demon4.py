#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/9/18 22:46
# @Author  : lingxiangxiang
# @File    : demon4_test.py


import MySQLdb
from DBUtils.PooledDB import PooledDB


db_config = {
        "host": "192.168.48.128",
        "port": 3306,
        "user": "xiang",
        "passwd": "123456",
        "db": "python",
        "charset": "utf8"
}

pool = PooledDB(creator=MySQLdb, mincached=5, blocking=True, **db_config)



if __name__ == "__main__":
    cnx = pool.connection()
    cus = cnx.cursor();
    SQL = "select * from tmp;"
    try:
        cus.execute(SQL)
        result = cus.fetchall()
        print(result)
        cus.close()
        cnx.commit()
    except Exception as e:
        raise e
    finally:
        cnx.close()

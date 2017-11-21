#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/9/24 0:13
# @Author  : lingxiangxiang
# @File    : demon12.py




import MySQLdb

# 把分数小于5分的成绩都加6分
sql = '''alter table score add index idx_stdid_couid(std, couid)'''
sql1 = '''alter table score add index idx_couid_stdid(couid, std)'''


def connect_mysql():
    db_config = {
        "host": "192.168.48.131",
        "port": 3306,
        "user": "ling",
        "passwd": "123456",
        "db": "stuteas",
        "charset": "utf8"
    }
    try:
        cnx = MySQLdb.connect(**db_config)
    except Exception as e:
        raise e
    return cnx

if __name__ == "__main__":
    cnx = connect_mysql()
    cus = cnx.cursor()
    try:
        cus.execute(sql)
        result1 = cus.fetchall()
        print(result1)

        cus.close()
        cnx.commit()
    except Exception as e:
        cnx.rollback()
        raise e
    finally:
        cnx.close()


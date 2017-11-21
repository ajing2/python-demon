#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/9/23 14:51
# @Author  : lingxiangxiang
# @File    : demon9.py

# 查询数据库
import codecs

import MySQLdb

select_student = '''select * from student where stdname in (select stdname from student  group by stdname having count(1)>1) order by stdname;'''
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
        cus.execute(select_student)
        result = cus.fetchall()
        print(result)
        with codecs.open("select.txt", "w") as f:
            for line in result:
                f.write(str(line))
                f.write("\n")
        cus.close()
        cnx.commit()
    except Exception as e:
        cnx.rollback()
        raise e
    finally:
        cnx.close()


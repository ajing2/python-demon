#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/9/23 16:42
# @Author  : lingxiangxiang
# @File    : demon10.py
import MySQLdb

sql = '''delete from teacher WHERE tid in (select tid from ((select score.couid, course.tid, score.grade, count(course.tid) as count_teacher from score join course on course.couid = score.couid and score.grade <60 join teacher on teacher.tid = course.tid GROUP BY course.tid ORDER BY count_teacher DESC LIMIT 5) as tid_test));'''

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
        cus.close()
        cnx.commit()
    except Exception as e:
        cnx.rollback()
        raise e
    finally:
        cnx.close()
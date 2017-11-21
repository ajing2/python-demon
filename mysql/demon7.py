#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/9/22 23:15
# @Author  : lingxiangxiang
# @File    : demon7.py
import MySQLdb


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

student = '''
    create table student(
        stdid int primary key not null,
        stdname varchar(100) not null,
        gender enum('F', 'M'),
        age int
    );
'''
course = '''
    create table course(
        couid int primary key not null,
        cname varchar(100) not null,
        tid int not null
    )
'''

score = '''
    create table score(
        sid int primary key not null,
        std int not null,
        couid int not null,
        grade int not null
    );
'''

teacher = '''
    create table teacher(
        tid int primary key not null,
        tname varchar(100) not null
    );

'''

tmp = '''
    set @a = 0;
    create table tmp as select (@a := @a +1) as id from information_schema.tables limit 10;
'''

if __name__ == "__main__":
    cnx = connect_mysql()
    print(cnx)
    print(dir(cnx))
    cus = cnx.cursor()
    try:
        cus.execute(student)
        cus.execute(course)
        cus.execute(score)
        cus.execute(teacher)
        cus.execute(tmp)
        cus.close()
        cnx.commit()
    except Exception as e:
        cnx.rollback()
        raise e
    finally:
        cnx.close()

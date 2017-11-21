#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/9/23 13:05
# @Author  : lingxiangxiang
# @File    : demon8.py


# selct * from tmp;      10行数据
# select * from tmp a, tmp b, tmp c;     1000行数据 = 10 * 10 * 10
# 表1， 表2， 表3


# student
# stdid   int
# stdname   varchar(100)
# gender   enum("F", "M")
# age  int

#
#

# 获得随机字符串的设计
# 增加的数据是随机数据,     rand()     函数生成0-1 的一个随机数
# sha1()   对数字进行加密，然后就生成了一堆字符串
# concat()    拼接多个字符串的函数
# substr（）    取多少个字符



# 获得随机整数的设计
# rand() * 50        0-50
# floor()  这个函数代表的是去尾法取整数


# 男女的设计
# rand() * 10   /2      最后取余数
# 如果余数为1， 就设置为M
# 如果余数为0， 就设置为F
import MySQLdb

student = '''
    set @a = 10000;
    insert into student select @a := @a + 1, substr(concat(sha1(rand()), sha1(rand())), 1, 5+floor(rand()* 50)), case floor(rand()*10) mod 2 when 1 then "M" else "F" end, 20+floor(rand() * 8) from tmp a, tmp b, tmp c, tmp d;
'''
# insert into student select @i:=@i+1, substr(concat(sha1(rand()), sha1(rand())), 1, 3 + floor(rand() * 75)), case floor(rand()*10) mod 2 when 1 then 'M' else 'F' end, 25-floor(rand() * 5)  from tmp a, tmp b, tmp c, tmp d;
# 我用下去这种insert就会有同名字的学生名


course = '''set @i := 10;
            insert into course select @i:=@i+1, substr(concat(sha1(rand()), sha1(rand())), 1, 5 + floor(rand() * 45)),  100 + floor(rand() * 100) from tmp a;
'''

score = '''set @i := 10000;
            insert into score select @i := @i +1, floor(10001 + rand()*10000), floor(11 + rand()*10), floor(1+rand()*100) from tmp a, tmp b, tmp c, tmp d;
'''
teacher = '''set @i := 100;
           insert into teacher select @i:=@i+1, substr(concat(sha1(rand()), sha1(rand())), 1, 5 + floor(rand() * 80)) from tmp a, tmp b;
'''


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
    try:
        cus = cnx.cursor()
        cus.execute(student)
        cus.close()

        cus = cnx.cursor()
        cus.execute(course)
        cus.close()

        cus = cnx.cursor()
        cus.execute(score)
        cus.close()

        cus = cnx.cursor()
        cus.execute(teacher)
        cus.close()

        cnx.commit()
    except Exception as e:
        cnx.rollback()
        raise e
    finally:
        cnx.close()
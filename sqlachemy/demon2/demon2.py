#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/11 22:09
# @Author  : lingxiangxiang
# @File    : demon2.py

def main():
    from util import CreateConnect
    sql = '''
          create table student(
            id int not null primary key,
            name varchar(50),
            age int,
            address varchar(100));
        '''
    cc = CreateConnect(username='xiang', password='xiang', host='192.168.48.131', dbname='sqlalchemy', dbtype='mysql')
    cc.get_connect()
    cc.execute(sql=sql)

if __name__ == "__main__":
    main()

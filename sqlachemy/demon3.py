#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/11 22:43
# @Author  : lingxiangxiang
# @File    : demon3.py
from sqlalchemy import MetaData, Table, Column, Integer, String

from sqlachemy.demon2.util import CreateConnect

def main():
    cc = CreateConnect(username='xiang', password='xiang', host='192.168.48.131', dbname='sqlalchemy', dbtype='mysql')
    engine = cc.creteEngine()
    metadata = MetaData(engine)
    user = Table('student', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String(20)),
                 Column('fullname', String(40))
                 )
    metadata.create_all(engine)

if __name__ == '__main__':
    main()


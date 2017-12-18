#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/11 22:03
# @Author  : lingxiangxiang
# @File    : util.py
from sqlalchemy import create_engine


class CreateConnect(object):
    def __init__(self, username, password, host, dbname, dbtype):
        # self.sql = sql
        self.username = username
        self.password = password
        self.host = host
        self.dbname = dbname
        self.dbtype = dbtype
        self.engine = create_engine('{0}://{1}:{2}@{3}/{4}'.format(self.dbtype, self.username, self.password, self.host, self.dbname))
        self.conn = None

    def creteEngine(self):
        self.engine = create_engine('{0}://{1}:{2}@{3}/{4}'.format(self.dbtype, self.username, self.password, self.host, self.dbname))
        return self.engine

    def get_connect(self):
        self.conn = self.engine.connect()

    def execute(self, sql):
        self.conn.execute(sql)
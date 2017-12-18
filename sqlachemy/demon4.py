#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/17 23:33
# @Author  : lingxiangxiang
# @File    : demon4.py
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://xiang:xiang@192.168.48.131/sqlalchemy')
Base = declarative_base()
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    address = Column(String(100))

student1 = Student(id=1009, name="ajing", age=20, address="beijing")
student2 = Student(id=1111, name="ling", age=202, address="beijing")
student3 = Student(id=1112, name="shang", age=100, address="beijing")

DBsession = sessionmaker(bind=engine)
session = DBsession()
# session.add(student1)
session.add_all([student2, student3])
session.commit()
session.close()
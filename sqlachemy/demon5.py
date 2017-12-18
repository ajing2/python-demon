#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 22:37
# @Author  : lingxiangxiang
# @File    : demon5.py
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    address = Column(String(100))

def getSession():
    engine = create_engine('mysql://xiang:xiang@192.168.48.131/sqlalchemy')
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    return session


if __name__ == "__main__":
    session = getSession()
    student1 = session.query(Student).filter_by(name="ajing").first()
    print(student1)
    print(student1.id, student1.name, student1.age, student1.address)

    student2 = session.query(Student).filter(Student.name.in_(['ajing', 'ling'])).all()
    print(student2)
    # print(student2.id, student2.name, student2.age, student2.address)
    students = session.query(Student).filter(Student.name.like("%in%")).order_by(Student.id.desc()).all()
    # for i in students:
    #     print(i.id)





#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/28 11:04
# @Author  : lingxiangxiang
# @File    : test1.py


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
while True:
    cmd = raw_input('please input cmd:>')
    if cmd == 'quit':
        break
    if cmd == '':
        continue
    s.sendall(cmd)
    data = s.recv(2048)
    print data
s.close()


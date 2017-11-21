#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/26 14:40
# @Author  : lingxiangxiang
# @File    : test.py
import commands
import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 8888
address = (host, port)
s.bind(address)
s.listen(10)

while 1:
    conn, addr = s.accept()
    print('connect by {0}'.format(addr))
    while 1:
        data = conn.recv(2048)
        if not data:
            print('byebye!')
            break
        print(data)
        # cmd_status, cmd__result = commands.getstatusoutput('data')
        # conn.send(cmd__result)
        # content = os.popen(data).read()
        conn.send(data + '  return')
s.close()



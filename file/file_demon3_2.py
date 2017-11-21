#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/30 15:39
# @Author  : lingxiangxiang
# @File    : file_demon3_2.py
import codecs

file = codecs.open('file3_2.txt', 'wb')
print(dir(file))
file.write('hello wolrd!\nlingxiangxinag\n')
print(file.tell())
file.writelines(['aaaaa\n', 'bbbbb\n', 'ccccc\n', 'ddddd\n'])
print(file.tell())
file.flush()
file.seek(0)
file.write('this theacher is so very very cool!!!!')
print(file.name)
print(file.closed)
print(file.encoding)
print(file.mode)
file.close()
print(file.closed)




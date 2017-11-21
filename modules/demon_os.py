#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/6 21:28
# @Author  : lingxiangxiang
# @File    : demon_os.py
import os

# 1，查看不通的操作系统
print(os.name)
# linux 系统os.name 是posix
# windows系统 os.name 是nt

# 2, 执行系统命令

# print(os.system('ipconfig'))
# windows的格式是 gkm
# 常用的utf-8
context = os.popen('ipconfig').read()
# print(context)
print(context.find('192.168.48.1'))
print(dir(os))
# 3. 文件和目录的操作

print(os.listdir('.'))
print(os.getcwd())
print(os.listdir(os.getcwd()))

# os.chdir(r'E:\test')
# print(os.getcwd())
# os.mkdir('test')
# os.remove('ling.log')
print(os.linesep)

if not os.path.exists('test'):
    os.makedirs('test')
else:
    print('test mulu is ok!')

a = os.path.join('.', 'aaa', 'bbb', 'ccc')
print(a)


print(os.path.dirname(r'E:\test\test.py'))

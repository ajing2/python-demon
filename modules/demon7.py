#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/18 23:12
# @Author  : lingxiangxiang
# @File    : demon7.py

# ansible -i 1.txt all -m shell -a 'w'
#shell  $1   $2  $3
# sys.argv[n]  可以获取到python脚本后面传进去的参数
import sys


def hello():
    print('hello world')
if __name__ =='__main__':
    print('sys.argv[0] = {0}'.format(sys.argv[0]))
    print('sys.argv[1] = {0}'.format(sys.argv[1]))
    print('sys.argv[2] = {0}'.format(sys.argv[2]))
    # print('aaaaaaaaa')
    # sys.stdout.write('hello lingxinagxinag\n')
    # print('hello world')
    # name = raw_input('Please input your name: ')
    # print('hello ' + name)
    # address = sys.stdin.readline()
    # print(address)
    # f = open('1.log', 'w')
    # sys.stdout = f
    # print('aaaaa')
    # print('hello wolrd')
# sys.exit(n)

    sys.exitfunc = hello
    print('start')
    sys.exit(1)
    print('end')

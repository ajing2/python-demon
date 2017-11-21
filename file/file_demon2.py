#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/30 14:41
# @Author  : lingxiangxiang
# @File    : file_demon2.py
import codecs
# codecs  这个模块主要是用来解决文件乱码的问题
# open(filename, mode)
# mode有几个参数需要学习：
# r    读
# w    写
# b    二进制
# a    追加
f = codecs.open('2.txt', 'ab')
f.write('hello world!\n')
f.write('hello {0}\n'.format('ling'))
f.write('hello %s\n' %'meizi')
f.write('you are very very cool!\n')
f.write('we love this theacher!\n')
f.close()



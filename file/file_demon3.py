#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/30 14:57
# @Author  : lingxiangxiang
# @File    : file_demon3.py
import codecs
# readlines()方法：读取文件内容，文件内容的每一行都是一个字符换，最后返回一个list
f = codecs.open('2.txt', 'rb')
print(dir(f))
# help(f.flush)
# help(f.seek)
text_list = f.readlines()
# print(type(text_list))
# print(text_list)
# print(f.readlines())
# print(text_list[0])
f.close()

# readline() 读取文件一行内容，返回一个字符串
# next() 读取文件下一行内容返回一个字符串
f = codecs.open('2.txt', 'rb')
print(f.readline())
# print(f.readline())
# print(f.readline())
print(f.next())
f.close()

# wirte() 必须传入字符串   read()
# writelines()   必须穿入一个序列

f = open('file3.txt', 'wb')
f.write('hello world\nsdkjflsadjfsa\nasldjflsadjf\nsdlfjasld\n')
print(f.tell())
f.seek(12)
print(f.tell())
f.writelines(['aaaaaa\n', 'bbbbbbb\n', 'ccccccccc\n'])
f.close()


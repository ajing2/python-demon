#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/30 14:31
# @Author  : lingxiangxiang
# @File    : file_demon1.py
import codecs
# 打开文件需要几步：
# 1. open文件
# 2. 文件操作（读或者写）
# 3. 关闭文件
f = codecs.open('1.txt')
text = f.read()
print(type(text))
result = text.replace('1', 'A')
print(result)
# print(f.read())
print(dir(f))
f.close()



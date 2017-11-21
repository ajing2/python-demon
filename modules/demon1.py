#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/25 18:27
# @Author  : lingxiangxiang
# @File    : demon1.py
import ling.test
ling.test.hello()


# 这样写是不是感觉比较麻烦


from ling import test
test.hello()


import ling.test as aaa
print('aaaaaaaaaaaaaaaaaaaaaa')
aaa.hello()
print('aaaaaaaaaaaaaaaaaaaaaa')

# import  一般我们用作导入模块来用，常用的快捷键是  alt + enter 就可以直接导入模块

# from ... import ...  这个是从什么模块中导入什么,最终你可以导入的是一个函数，也可以是一个类，也可以是一个模块
# 总结：就是一层一层的调用就可以了
# 注意： 1. import后面导入的是什么，在调用的时候，就必须写什么，除非你用from进行导入，
#        2. 导入的时候不写后缀名字



from ling.test import hello
hello()




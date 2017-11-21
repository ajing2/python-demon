#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/24 22:50
# @Author  : lingxiangxiang
# @File    : demon2.py


import timeit
print timeit.timeit(setup='''import re; reg = re.compile('<(?P<tagname>\w*)>.*</(?P=tagname)>')''', stmt='''reg.match('<h1>xxx</h1>')''', number=1000000)
print timeit.timeit(setup='''import re''', stmt='''re.match('<(?P<tagname>\w*)>.*</(?P=tagname)>', '<h1>xxx</h1>')''', number=1000000)
#
# 1.正则匹配是，优先编译成正则对象，然后在进行匹配，这样程序的效率要高，


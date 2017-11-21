#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/25 0:05
# @Author  : lingxiangxiang
# @File    : demon5.py

import re
p = re.compile(r'(\w+) (\w+)')
s = 'i say,,,,,, hello world!'
print(p.sub(r'\2 \1', s))
def func(m):
    return m.group(1).title() + 'aaaaaaaaa ' + m.group(2).title()
print(p.sub(func, s))




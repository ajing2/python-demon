#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/25 21:56
# @Author  : lingxiangxiang
# @File    : demon4_test.py

import logging

# logging.debug('this is debug message.')
# logging.info('this is info message.')
# logging.warning('this is warning message.')
# logging.error('this is error message.')
# logging.critical('this is critical message.')

# 从上往下，日志级别逐渐升高，debug->info->warning->error->critical

print('###################################')

logging.basicConfig(level=__debug__, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt=' %Y/%m/%d %H:%M:%S', filename='ling.log', filemode='w')
# logger = logging.getLogger(__name__)
logger = logging.getLogger()
logging.debug('thisaaa is debug message.')
logging.info('thisaaa is info message.')
logging.warning('thisaaa is warning message.')
logging.error('thisaaa is error message.')
logging.critical('thisaaa is critical message.')

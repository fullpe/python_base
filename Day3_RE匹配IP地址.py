# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author : zunsi
# @File   : RE匹配IP地址.py
# @Time   : 2019-10-20  21:25:34


import re

str1 = 'Port-channel1.189   192.168.189.254   YES   CONFIG   up   up'

re_result = re.match(r'(\w\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\w+\s+(up|down)\s+\w+',
                     str1.strip()).groups()

print(re_result)

format_str = '{0:<7}:  {1:50}'

print(format_str.format('接  口', re_result[0]))
print(format_str.format('IP地址', re_result[1]))
print(format_str.format('状  态', re_result[2]))

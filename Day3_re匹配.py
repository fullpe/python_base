# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file    : re匹配.py
# @time    : 2019-10-21  11:28:40


import re


str1 = '166 54a2.74f7.0326 DYNAMIC Gig1/0/11'
str2 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09,bytes 27575949, flags UIO'


re_result1 = re.match(r'(\d{1,4})\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\w+)\s+(\w\S+\d)', str1.strip()).groups()
re_result2 = re.match(r'(\w+)\s+server\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})\s+localserver\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}),\s+idle\s+(\d{1,2}):(\d{1,2}):(\d{1,2}),bytes\s+(\d+),\s+flags\s+(\w+)', str2.strip()).groups()


print(re_result1)
print(re_result2)


format_str1 = '{0:<} : {1:<50}'
print('='* 100)
print(format_str1.format('VLAN ID ',  re_result1[0]))
print(format_str1.format('MAC 地址', re_result1[1]))
print(format_str1.format('接口类型',  re_result1[2]))
print(format_str1.format('接   口 ', re_result1[3]))
print('='* 100)


format_str2 = '{0:<20}:  {1:50}'

str_idle = '{0}小时 {1}分钟 {2}秒'.format(re_result2[3], re_result2[4], re_result2[5])

print('=' * 100)
print(format_str2.format('protocol ',  re_result2[0]))
print(format_str2.format('server', re_result2[1]))
print(format_str2.format('localserver',  re_result2[2]))
print(format_str2.format('idle', str_idle))
print(format_str2.format('bytes', re_result2[6]))
print(format_str2.format('flags', re_result2[7]))
print('=' * 100)

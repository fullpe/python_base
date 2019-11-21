# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file    : 第五天re匹配路由.py
# @time    : 2019-10-22  18:18:22


import os
import re

# # 实现1：
# route_n = os.popen('route -n').readlines()[2:]
#
# route_1 = route_n[0]
#
# gw = re.findall(r'0.0.0.0\s+(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3})', route_1)[0]
#
# print('网关为：', gw)

# 实现二：
#
# import re
# import os
#
# route_result = os.popen('route -n').readlines()[2:]
#
# for route_line in route_result:
#     route_gw = re.findall(r'\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\s+'
#                           r'(\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3})\s+'
#                           r'\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\s+'
#                           r'\w\w\s+\d+\s+\d+\s+\d+\s+ens32', route_line.strip())
#     route_ug = re.findall(r'\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\s+'
#                           r'\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\s+'
#                           r'\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\s+'
#                           r'(\w\w)\s+\d+\s+\d+\s+\d+\s+ens32', route_line.strip())
#
#     if route_ug[0] == 'UG':
#         print('网关为：', route_gw[0])
#         break


import re
import os

route_result = os.popen('route -n').readlines()[2:]


for route_line in route_result:
    route_gw = re.match(r'0\.0\.0\.0\s+(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3})\s+'
                        r'\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}\s+(\w\w)\s+\d+\s+\d+\s+\d+\s+ens', route_line.strip('\n')).groups()
    if route_gw[1] == 'UG':
        print('网关为：', route_gw[0])
        break

# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file    : Day6_sorted-lambda.py
# @time    : 2019-10-25  10:35:02


import re


port_list = ['eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7', 'eth 1/101/2/46', 'eth 1/101/1/34',
             'eth 1/101/1/18', 'eth 1/101/1/13', 'eth 1/101/1/32', 'eth 1/101/1/25', 'eth 1/101/1/45', 'eth 1/101/2/8']


print(sorted(port_list, key=lambda x: (int(re.findall(r'\d+', x)[0]),
                                       int(re.findall(r'\d+', x)[1]),
                                       int(re.findall(r'\d+', x)[2]),
                                       int(re.findall(r'\d+', x)[3]))
             )
      )

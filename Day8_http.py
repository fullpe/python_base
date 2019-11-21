# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file    : Day8_http.py
# @time    : 2019-10-28  17:52:13



import os
import re
import time

while True:
    try:
        netstat_res = os.popen('netstat -tulnp | grep 80').read()
        #print(netstat_res)
        tcp80 = False
        for netstat in netstat_res.split('\n'):
            re_result = re.match(r'(tcp)\s+\d+\s+\d\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:80)\s+', netstat)
            if re_result:
                print('HTTP (TCP/80)  服务已经被打开')
                tcp80 = True
                break
        if tcp80:
            break
        print('TCP\80端口未打开，等待3秒钟\n重新开始监控80端口······')

        time.sleep(3)
    except KeyboardInterrupt:
        print('退出')
        break
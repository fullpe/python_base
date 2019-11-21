# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file    : Day8_kamene.py
# @time    : 2019-10-28  18:58:58


import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

from kamene.all import *


ip = []


def qytang_ping(ip='172.16.1.253'):
    ping = IP(dst=ip)/ICMP()
    ping_result = sr1(ping, timeout=3, verbose=False)
    #ping_result.show()
    print(ping)
    print(ping_result)

    # if ping_result:
    #     return ip, True
    # else:
    #     return ip, False


# if __name__ == '__main__':
#     ping_kong = qytang_ping('10.1.1.1')
#     print('sdfgdfg', qytang_ping('10.10.100.11'))
#     if ping_kong[1]:
#         print(f'Ping测试： {ping_kong[0]}      结果：通过！')
#         print(ping_kong[1])
#     else:
#         print(f'Ping测试： {ping_kong[0]}      结果：不通过！')


# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file    : Day10_ping_paramiko.py
# @time    : 2019-10-30  11:12:54

import re
import pprint
from Day8_kamene_ping import qytang_ping
from Day9_paramiko_ssh import qytang_ssh


def qytang_get_if(*ips, user='jsonmedia', passwd='jsonmedia@2019'):
    device_if = {}
    for ip in ips:
        #print(ip)
        if_dict = {}
        if qytang_ping(ip):
            #print(if_dict)

            line = qytang_ssh(ip, user, passwd, cmd='dir')
                #re_interface = re.findall(r'(\w+:) flags=', line.strip(''))
                #re_inet4 = re.findall(r'(inet\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+', line.strip('\n'))
                #re_inet4 = re.match(r'\s+(inet\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+', line.strip('\n')).groups()
                #re_netmask = re.findall(r'\s+(netmask\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+', line.strip('\n'))
                #re_result = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line.strip())
                #re_result = (re_interface + re_inet4 + re_netmask)
                #print(re_inet4)
            print(line)


if __name__ == "__main__":
    #pprint.pprint(qytang_get_if('10.20.60.200'), indent=4)
    pprint.pprint(qytang_get_if('192.168.111.100'), indent=4)

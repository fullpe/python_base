# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file    : re表达式测试练习.py
# @time    : 2019-10-21  17:42:02

import os
import re

ifconfig_result = os.popen('ifconfig ' + 'ens32').read()

print(ifconfig_result)

ip = re.findall(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
netmask = re.findall(r'netmask (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
broadcast = re.findall(r'broadcast (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
mac = re.findall(r'ether ([A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2})',
                 ifconfig_result)[0]

print(ip, netmask, broadcast, mac)

ip_split = ip.split('.')
ip_split[3] = '1'
gw_ip = '.'.join(ip_split)
#gw = ip_split[0] + '.' + ip_split[1] + '.' + ip_split[2] + '.' + '1'
# gw = os.popen('route').read()
print(gw_ip)
format_str1 = '{0:<10} : {1:<50}'

print(format_str1.format('ipv4_add', ip))
print(format_str1.format('netmask', netmask))
print(format_str1.format('broadcase', broadcast))
print(format_str1.format('mac_addr', mac))

#print('=' * 100)
ping = os.popen('ping ' + gw_ip + ' -c 4').read()
print(ping)
ping_result = re.findall(r'\d\s+packets\s+transmitted,\s+(\d)\s+received', ping)[0]
print(ping_result)


print('假设网关IP地址最后一位为1，因此10.20.60.1')
if ping_result:
    print('网关: {0} ;  {1} 次可达'.format(gw_ip, ping_result))
else:
    print('{0} 网关不可达'.format(gw_ip))



#作业提交版本
# import os
# import re
#
# ifconfig_result = os.popen('ifconfig ' + 'ens32').read()
#
# ip = re.findall(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
# netmask = re.findall(r'netmask (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
# broadcast = re.findall(r'broadcast (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
# mac = re.findall(r'ether ([A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2})',
#                  ifconfig_result)[0]
#
# ip_split = ip.split('.')
#
# ip_split[3] = '1'
#
# gw_ip = '.'.join(ip_split)
#
# format_str1 = '{0:<10} : {1:<50}'
#
# print('=' * 80)
# print(format_str1.format('ipv4_add', ip))
# print(format_str1.format('netmask', netmask))
# print(format_str1.format('broadcase', broadcast))
# print(format_str1.format('mac_addr', mac))
# print('=' * 80)
#
# ping = os.popen('ping ' + gw_ip + ' -c 4').read()
#
# ping_result = re.findall(r'\d\s+packets\s+transmitted,\s+(\d)\s+received', ping)[0]
#
# print('假设网关IP地址最后一位为1，因此\n')
#
# if ping_result:
#     print('网关: {0} ;  {1} 次可达'.format(gw_ip, ping_result))
# else:
#     print('{0} 网关不可达'.format(gw_ip))
# print('=' * 80)

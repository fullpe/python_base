# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file    : ASA防火墙状态信息表（第六天）.py
# @time    : 2019-10-24  10:23:03


import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n \
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

# print(asa_conn.strip('\n'))
#
# i = re.match(r'\w+\s+\w+ (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s+'
#              r'\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}),\s+'
#              r'idle\s+\d{1,2}:\d{1,2}:\d{1,2},\s+'
#              r'bytes\s+(\d+),\s+'
#              r'flags\s+(\w+)'
#              , asa_conn.strip()).groups()
# print('=' * 50)
# print(i)
asa_dit = {}
for conn in asa_conn.split('\n'):
    #print(conn)
    #rec = re.match(r'\w', conn)
    #print(rec)
    re_result = re.match(r'\w+\s+\w+ (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s+'
                         r'\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}),\s+'
                         r'idle\s+\d{1,2}:\d{1,2}:\d{1,2},\s+'
                         r'bytes\s+(\d+),\s+'
                         r'flags\s+(\w+)'
                         , conn.strip()).groups()
    asa_dit[re_result[:4]] = re_result[4:]

print(asa_dit)

src = 'src'
dst = 'dst'
src_port = 'src_port'
dst_port = 'dst_port'
bytes_id = 'bytes'
flags_id = 'flags'

for key, value in asa_dit.items():
    l = len(f'{src:^8} :{key[0]:^20}|   {src_port:^10}:{key[1]:^8}|{dst:>8} :{key[2]:^18}| {dst_port:^10}:{key[3]:^8}|')
    print('=' * l)
    print(f'{src:^8} :{key[0]:^20}|   {src_port:^10}:{key[1]:^8}|{dst:>8} :{key[2]:^18}| {dst_port:^10}:{key[3]:^8}|')
    print(f'{bytes_id:^8} :{value[0]:^20}|   {flags_id:^10}:{key[1]:^8}|\n')
    print('=' * l)

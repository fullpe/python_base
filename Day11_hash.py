# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author : zunsi
# @File   : Day11_hash.py
# @Time   : 2019-10-31  22:39:12


from Day9_paramiko_ssh import qytang_ssh
import re
import hashlib
import time


def qytang_get_config(ip, username='admin', password='admin888'):
    try:
        device_config_sh = qytang_ssh(ip, username, password, cmd='show run')
        #print(device_config_sh)
        split_result = re.split(r'\r\nhostname \S+\r\n', device_config_sh)
        device_config = device_config_sh.replace(split_result[0], '').strip()
        return device_config
    except Exception:
        return


def qytang_check_diff(ip, username='admin', password='admin888'):
    before_md5 = ''
    while True:
        device_config = qytang_get_config(ip, username, password)
        m = hashlib.md5()
        m.update(device_config.encode())
        md5_value = m.hexdigest()
        print(md5_value)
        if not before_md5:
            before_md5 = md5_value
        elif before_md5 != md5_value:
            print('MD5 value changed')
            break
        time.sleep(5)


if __name__ == '__main__':
    #print(qytang_get_config('192.168.111.100', username='admin', password='admin888'))
    print(qytang_check_diff('192.168.111.100', username='admin', password='admin888'))

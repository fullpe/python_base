# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file    : Day9_paramiko获取网关地址.py
# @time    : 2019-10-29  11:25:32


import paramiko
import re


def ssh_conn(ip, user, passwd,  port=22, cmd='dir', timet=5, comp=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=user, password=passwd, timeout=timet, compress=comp)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.read().decode()


def ssh_gw(ip, user, passwd):
    gw_result = ssh_conn(ip, user, passwd, cmd='route -n')

    for routen in gw_result.split('\n')[2:-1]:
        gw = re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                      '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+(\w\w)\s+\d\d\d', routen.strip())
        if routen:
            if gw.groups()[1] == 'UG':
                return gw.groups()[0]


if __name__ == '__main__':
    print(ssh_conn('10.20.60.200', 'root', 'ubuntu'))
    print('网关地址为：\n', ssh_gw('10.20.60.200', 'root', 'ubuntu'))

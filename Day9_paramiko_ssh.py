# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file    : Day9_paramiko初探.py
# @time    : 2019-10-29  10:58:31


import paramiko
import time

# ssh = paramiko.SSHClient()
# ssh.load_system_host_keys()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh.connect('10.20.60.200', port=22, username='root', password='ubuntu', timeout=5, compress=True)
# # ssh.connect('10.10.100.11', port=22, username='jsonmedia', password='jsonmedia@2019', timeout=5, compress=True)
#
# stdin, stdout, stderr = ssh.exec_command('dir')
#
# x = stdout.read().decode()
#
# print(x)


def qytang_ssh(ip, user, passwd, port=22, cmd='dir', timet=1, comp=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=user, password=passwd, timeout=timet, compress=comp)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    #print(stdin().decode)
    return stdout.read().decode()


if __name__ == '__main__':
    #print(ssh('10.20.60.200', 'root', 'ubuntu', cmd='dir'))
    print(qytang_ssh('10.10.100.11', 'jsonmedia', 'jsonmedia@2019', cmd='ping 1.1.1.1'))


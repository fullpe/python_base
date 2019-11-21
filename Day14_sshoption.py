# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author : zunsi
# @File   : Day14_sshoption.py
# @Time   : 2019-11-05  20:27:40


import paramiko


def qytang_ssh(ip, username, password, cmd='ifconfig', port=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    f = stdout.read().decode()
    return f


if __name__ == "__main__":
    from argparse import ArgumentParser

    usage = "usage: python Simple_SSH_Client.py -i ipaddr -u username -p password -c command"

    parser = ArgumentParser(usage=usage)

    parser.add_argument("-i", "--ipaddr", dest="ipaddr", help="SSH Server", default="172.16.1.254", type=str)
    parser.add_argument("-p", "--port", dest="ports", help="SSH Port", default="22", type=str)
    parser.add_argument("-u", "--username", dest="username", help="SSH Username", default="admin", type=str)
    parser.add_argument("-pwd", "--password", dest="password", help="SSH Password", default="admin", type=str)
    parser.add_argument("-c", "--command", dest="command", help="Shell Command", default="ls", type=str)

    args = parser.parse_args()

    print(qytang_ssh(ip=args.ipaddr, port=args.ports, username=args.username, password=args.password, cmd=args.command))

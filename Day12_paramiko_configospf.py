# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author : zunsi
# @File   : Day12_paramiko_configospf.py
# @Time   : 2019-11-01  19:39:01


import paramiko
import time


# def buffer_result(stream):
#     buffer = []
#     while True:
#         # 接受数据
#         stream_result = stream.recv(1024).decode('utf-8')
#         # 接收到的数据缓存到buffer中，直到返回空数据结束
#         if stream_result:
#             buffer.append(stream_result)
#         else:
#             break
#     # 拼接数据
#     data = b''.join(buffer)
#     # 返回完整的数据
#     print(data)
#     return data


#定义SSH函数
def ssh_multicmd(ip, user, passwd, cmd_list, enable='', wait_time=3, ports=22, verbose=True, timeouts=10, compresss=True):
    # 创建SSH Client
    ssh = paramiko.SSHClient()
    # 加载本地密钥
    ssh.load_system_host_keys()
    # 设置自动添加远程主机名及其密钥到本地
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # SSH 连接
    ssh.connect(ip, username=user, password=passwd, port=ports, timeout=timeouts, compress=compresss)
    # 开始交互式会话连接
    chan = ssh.invoke_shell()
    time.sleep(1)
    x = chan.recv(4096).decode()
    # x = buffer_result(chan)

    if enable and '>' in x:
        chan.send('enable'.encode())
        chan.send(b'\n')
        time.sleep(1)
        chan.send(enable.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
    elif not enable and '>' in x:
        print('缺少enable密码')
        return

    for cmd in cmd_list:
        chan.send(b'\n')
        chan.send(cmd.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
        x = chan.recv(40960).decode()
        #x = buffer_result(chan)
        if verbose:
            print(x)

    # 结束交互式会话连接
    chan.close()
    # 结束ssh连接
    ssh.close()


if __name__ == '__main__':
    ssh_multicmd('192.168.111.100', 'admin', 'admin888',
                 ['terminal length 0',
                  'show version',
                  'config ter',
                  'router ospf 1',
                  'network 192.168.111.100 0.0.0.255 area 0',
                  'end',
                  'show run | sec router',
                  ],
                 enable='admin888',
                 wait_time=2,
                 #verbose=False
                 )


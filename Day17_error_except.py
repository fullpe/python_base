# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author : zunsi
# @File   : Day17_error_except.py
# @Time   : 2019-11-08  21:19:32


import sqlite3
import re
import hashlib
import paramiko
import socket


def qytang_ssh(ip, username, password, cmd='ls', port=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    except paramiko.ssh_exception.AuthenticationException as e:
        print("Error !  认证失败", e)
        return
    except socket.timeout as e:
        print("Error !  连接超时", e)
        return
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        print("Error !  SSH请求被管理列表过滤", e)
        return
    else:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        i = stdout.read().decode()
        if 'Line has invalid autocommand' in i:
            print("Error ! 命令未执行! 请检查用户权限!")
            return
        else:
            return i


# def get_config_md5(ip, username='admin', password='admin888'):
#     try:
#         device_config_raw = qytang_ssh(ip, username, password, cmd='show run')
#         split_result = re.split(r'\r\nhostname \S+\r\n', device_config_raw)
#         device_config = device_config_raw.replace(split_result[0], '').strip()
#
#         md5 = hashlib.md5()
#         md5.update(device_config.encode())
#         md5_value = md5.hexdigest()
#         return device_config, md5_value
#     except Exception:
#         return


# device_list = ['192.168.111.100']
# username = 'admin'
# password = "admin888"
#
#
# def wirte_config_md5_to_db():
#     conn = sqlite3.connect('bakconfig.db')
#     cursor = conn.cursor()
#     for device in device_list:
#         ip_config_md5 = get_config_md5(ip=device, username=username, password=password)
#         cursor.execute('select * from config_md5 where ip=?', (device,))
#         md5_result = cursor.fetchall()
#         if not md5_result:
#             cursor.execute("insert into config_md5(ip, config, md5) values (?, ?, ?)", (device,
#                                                                                         ip_config_md5[0],
#                                                                                         ip_config_md5[1]))
#             conn.commit()
#         else:
#             if ip_config_md5[1] != md5_result[0][2]:
#                 cursor.execute("update config_md5 set config=?, md5=? where ip=?", (ip_config_md5[0],
#                                                                                    ip_config_md5[1],
#                                                                                    device))
#                 conn.commit()
#             else:
#                 continue
#     cursor.execute("select * from config_md5")
#     all_result = cursor.fetchall()
#     for x in all_result:
#         print(x[0], x[2])
#     conn.close()


if __name__ == "__main__":
    qytang_ssh('192.168.111.100', 'admin', 'admin', cmd='show run')
#     import os
#     if os.path.exists('bakconfig.db'):
#         os.remove('bakconfig.db')
#
#     conn = sqlite3.connect('bakconfig.db')
#     cursor = conn.cursor()
#     cursor.execute("create table config_md5 (ip varchar(40), config varchar(99999), md5 varchar(1000))")
#     conn.commit()
#     cursor.close()
#     conn.close()
#     wirte_config_md5_to_db()

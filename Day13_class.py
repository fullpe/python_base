# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author : zunsi
# @File   : Day13_class.py
# @Time   : 2019-11-04  20:37:47


import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *


class QYTANG:
    def __init__(self, ip):
        self.ip = ip
        self.length = 100
        self.srcip = ''

    def make_pkt(self):
        if self.srcip:
            self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b's' * self.length)
        else:
            self.pkt = IP(dst=self.ip) / ICMP() / (b's' * self.length)

    def one(self):
        self.make_pkt()
        result = sr1(self.pkt, timeout=1, verbose=False)
        if result:
            print(self.ip, '可达')
        else:
            print(self.ip, '不可达')

    def ping(self):
        self.make_pkt()
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)
        print()

    def __str__(self):
        if not self.srcip:
            return '<{0} => dstip: {1}, size:{2}>'.format(self.__class__.__name__, self.ip, self.length)
        else:
            return '<{0} => srcip: {1}, dstip: {2}, size:{3}>'.format(self.__class__.__name__, self.srcip, self.ip, self.length)


class NewPing(QYTANG):
    def ping(self):
        self.make_pkt()
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('+', end='', flush=True)
            else:
                print('？', end='', flush=True)
        print()



if __name__ == "__main__":
    ping = QYTANG('172.16.1.253')
    total_len = 70

    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word))/2), word, s * int((70 - len(word))/2)))
    print_new('print class')
    # 打印类
    print(ping)
    print_new('ping one for sure reachable')
    # ping测试
    ping.one()
    print_new('ping five')
    # ping 5次，"!"通，"."不通
    ping.ping()
    print_new('set payload lenth')
    # 更改负载长度
    ping.length = 200
    print(ping)    # 先打印看下类
    ping.ping()    # 进行ping测试
    print_new('set ping src ip address')
    # 修改源ip地址
    ping.srcip = '172.16.1.254'
    print(ping)
    ping.ping()
    print_new('new class NewPing', '=')
    newping = NewPing('172.16.1.253')
    newping.length = 300
    print(newping)
    newping.ping()

# !/usr/bin/python3
# -*- coding=utf-8 -*-
# @file: random ip.py
# @time: 2019-10-19  19:01:00


import random


def random_num1():
	num = random.randint(1, 254)
	return num


def random_num2():
	num = random.randint(0, 255)
	return num


def random_ip():
	ip = str(random_num1())+'.'+str(random_num2())+'.'+str(random_num2())+'.'+str(random_num2())
	return ip


if __name__ == '__main__':
	print(random_ip())

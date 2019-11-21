# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file    : Day8_list.py
# @time    : 2019-10-28  19:22:07




list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

#方法一：
# for x in list1:
#     if x in list2:
#         print(f'{x} in List1 and List2')
#     else:
#         print(f'{x} only in list1')

# for x in list1:
#     print(f'{x} in List1 and List2') if x in list2 else print(f'{x} only in List1')

def find_same(l1,l2):
    for x in l1:
        print(f'{x} in List1 and List2') if x in list2 else print(f'{x} only in List1')

if __name__ == '__main__':
    find_same(list1,list2)
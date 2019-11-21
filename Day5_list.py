# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file    : list(第五天).py
# @time    : 2019-10-23  18:22:37

# # 拷贝
# l1 = [4, 5, 7, 1, 3, 9, 0]
# l2 = l1.copy()
#
# print(id(l1))
# print(id(l2))
#
# for i in range(len(l1)):
#     print(l1[i], l2[i])



# 引用
l1 = [4, 5, 7, 1, 3, 9, 0]
l2 = l1

print(id(l1))
print(id(l2))

for i in range(len(l1)):
    print(l1[i], l2[i])

# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author : zunsi
# @File   : 字符串拼接.py
# @Time   : 2019-10-20  20:23:35

#拼接1
str1 = 'QYTANG'
str2 = '\''
str3 = 'day '
str4 = '2014-09-28'

line = str1 + str2 + str3 + str4

print(line)

#拼接2
str10 = ['QYTANG', '\'', 'day\000', '2014-09-28']

str_night = ''.join(str10)

print(str_night)

#拼接3
print('QYTANG\'day', '2014-09-28')

#拼接4
str_word = 'QYTANG\'{} {}'.format('day', '2014-09-28')
print(str_word)

#拼接5
str_word_index0 = 'QYTANG\'{0} {1}'.format('day', '2014-09-28')
str_word_index1 = 'QYTANG\'{1} {0}'.format('day', '2014-09-28')
print(str_word_index0)
print(str_word_index1)
# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author : zunsi
# @File   : osfile.py
# @Time   : 2019-10-24  23:13:37


import os

if os.path.isdir('test'):
    pass
else:
    os.mkdir('test')

os.chdir('test')


if os.path.isfile('qytang1'):
    pass
else:
    with open(os.getcwd() + '\\qytang1file', 'w') as qytang1:
        qytang1.write('test file\nthis is qytang\n')


if os.path.isfile('qytang2'):
    pass
else:
    with open(os.getcwd() + '\\qytang2file', 'w') as qytang2:
        qytang2.write('test file\nqytang python\n')


if os.path.isfile('qytang3'):
    pass
else:
    with open(os.getcwd() + '\\qytang3file', 'w') as qytang3:
        qytang3.write('test file\nthis is python DevNetOps\n')


if os.path.isdir('qytang4'):
    pass
else:
    os.mkdir('qytang4')


if os.path.isdir('qytang5'):
    pass
else:
    os.mkdir('qytang5')
    os.chdir('qytang5')
    with open(os.getcwd() + '\\qytang6file', 'w') as qytang6:
        qytang6.write('test file\nthis is qytang python DevNetOps\n')


############################################################
#方法一：
# for file_list in os.listdir(os.getcwd()):
#     #print(file_list)
#     if os.path.isfile(file_list):
#         for text in open(file_list):
#             if 'qytang' in text:
#                 print('==' * len(os.getcwd()))
#                 print('文件中包含“qytang”关键字的文件为：\t' + file_list + '\t')
#                 print('路径是：\t' + os.path.join(os.getcwd(), file_list))
#                 print('==' * len(os.getcwd()))
#                 break

############################################################



############################################################
#方法二：
os.chdir('..')
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for file in files:
        for text in open(os.path.join(root, file)):
            if 'qytang' in text:
                print('==' * len(os.getcwd()))
                print('文件中包含 “qytang” 关键字的文件为：\t' + file + '\t')
                print('路径是：\t' + os.path.join(root, file))
                print('==' * len(os.getcwd()))
                break

############################################################







# os.mkdir('test')
# os.chdir('test')
# qytang1 = open('qytang1', 'w')
# qytang1.write('test file\n')
# qytang1.write('this is qytang\n')
# qytang1.close()
# qytang2 = open('qytang2', 'w')
# qytang2.wirte('test file\n')
# qytang2.write('qytang python\n')
# qytang2.close()
# qytang3 = open('qytang3', 'w')
# qytang3.write('test file\n')
# qytang3.write('this is python\n')
# qytang3.close()
# os.mkdir('qytang4')
# os.mkdir('qytang5')
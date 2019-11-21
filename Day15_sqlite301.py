# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author : zunsi
# @File   : Day15_sqlite301.py
# @Time   : 2019-11-06  20:38:38


import sqlite3
import os

homework_dict = [{'姓名': '学员1', '年龄': 37, '作业数': 1},
                 {'姓名': '学员2', '年龄': 32, '作业数': 5},
                 {'姓名': '学员3', '年龄': 35, '作业数': 10}]

# 连接数据库
if os.path.exists('qytanghomework.sqlite'):
    os.remove('qytanghomework.sqlite')

conn = sqlite3.connect('qytanghomework.sqlite')
cursor = conn.cursor()

# 创建表
cursor.execute("create table qytang_homework_info(学员姓名 varchar(40), 学员年龄 int, 学员作业数 int)")

for teacher in homework_dict:
    name = teacher['姓名']
    age = teacher['年龄']
    homework = teacher['作业数']
    print(name, age, homework)
    #cursor.execute("insert into qytang_homework_info(姓名, 年龄, 作业数) values('{0}', {1}, {2})".format(name, age, homework))
    cursor.execute("insert into qytang_homework_info values (?, ?, ?)", (name, age, homework))
    #cursor.close()
    # # 查看表中的内容
    # cursor.execute("select * from qytang_homework_info")
    # results = cursor.fetchall()
    # for i in results:
    #     print(i)
conn.commit()
conn.close()

if __name__ == "__main__":
    pass



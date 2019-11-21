# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author : zunsi
# @File   : Day15_sqlite302.py
# @Time   : 2019-11-06  21:59:42


import sqlite3
import time

user_notify = """
请输入查询选项：

输入 1 ： 查询整个数据库
输入 2 ： 基于姓名查询
输入 3 ： 基于年龄查询
输入 4 ： 基于作业数查询
输入 0 ： 退出
"""


def search_result_str(search_sql):
    conn = sqlite3.connect("qytanghomework.sqlite")
    try:
        cursor = conn.cursor()
        all_search_info = cursor.execute(search_sql)
        #print(all_search_info.description)
        all_description = [des[0] for des in all_search_info.description]
        #print(all_description, '\n',)

        search_result = cursor.fetchall()
        if not search_result:
            return '学员信息未找到'
        return_str = ''
        for x in search_result:
            for y in zip(all_description, x):
                return_str += (f'{y[0]:>3}:{y[1]:<7}')
            return_str += '\n'

        cursor.close()
        #print(return_str)
        return return_str
    except Exception as e:
        #print('Error:  ', e)
        return 'Error ！！！搜索失败 ！'
    finally:
        conn.close()


while True:
    print(user_notify)
    user_input = input("请输入您的选择：  ")

    if user_input == '0':
        print('程序将在3秒钟后退出')
        time.sleep(3)
        break

    elif user_input == '1':
        print(search_result_str("select * from qytang_homework_info"))
        time.sleep(3)


    elif user_input == '2':
        user_name = input('请输入学员姓名：  ')
        if not user_name:
            continue
        print('=' * 60)
        print(search_result_str("select * from qytang_homework_info where 学员姓名 = '{0}'".format(user_name)))

    elif user_input == '3':
        user_age = input('搜索大于输入年龄的学员，请输入学员年龄：  ')
        if not user_age:
            continue
        print('=' * 60)
        print(search_result_str("select * from qytang_homework_info where 学员年龄 > '{0}'".format(user_age)))
    elif user_input == '4':
        user_hwork = input('搜索大于输入作业数的学员，请输入学员作业数量：  ')
        if not user_hwork:
            continue
        print('=' * 60)
        print(search_result_str("select * from qytang_homework_info where 学员作业数 > '{0}'".format(user_hwork)))

    else:
        print('\n' + '警      告!  搜索错误，请重新输入\n')


#a = search_result_str('select * from qytang_homework_info')
#print(a)































if __name__ == "__main__":
    pass
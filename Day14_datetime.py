# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author : zunsi
# @File   : Day14_datetime.py
# @Time   : 2019-11-05  19:58:53


from datetime import datetime, timedelta

# 获取当前时间
nowtime = datetime.now()
# 获取5天前的时间
FiveDaysLater = nowtime - timedelta(days=5)

# 生成文件名
FileName = 'save_FiveDaysLater_time_' + nowtime.strftime("%Y-%m-%d_%M-%S") + ".txt"

# 写入文件
with open(FileName, 'w') as f:
    f.write(str(FileName))


if __name__ == "__main__":
    print(FiveDaysLater)

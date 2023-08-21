# -*- coding: utf-8 -*-
# @Time  : 2023/08/18 10:14:22
# @Author: wy

from datetime import datetime, timedelta


def utf_time(time):
    creation_time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
    new_creation_time = creation_time + timedelta(hours=8)
    new_utc_time_str = new_creation_time.strftime('%Y-%m-%d')
    return new_utc_time_str


def now_time():
    current_date = datetime.now().date()
    new_current_date = current_date.strftime('%Y-%m-%d')
    return new_current_date
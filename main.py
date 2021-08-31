#!./usr/bin/env.python
# .-*- coding: utf-8 -*-
# ._author_.=."Max丶"
# ._Email:_.=."max@chamd5.org"
import time
from borax.calendars.lunardate import LunarDate
from QuXiang.QuXiang import *


def ShiChen():
    print(time.strftime("现在阳历时间为：%Y-%m-%d  %H:%M\n", time.localtime()))
    Year = int(time.strftime("%Y", time.localtime()))
    Month = int(time.strftime("%m", time.localtime()))
    Day = int(time.strftime("%d", time.localtime()))
    # 转换 农历年月日
    lunar_date = LunarDate.from_solar_date(Year, Month, Day)
    month = lunar_date.month
    day = lunar_date.day
    print(lunar_date.strftime('%G'))
    print('农历时间：', month, '月',day,'日','\n')
    print('以下是时辰对应的数字：')
    print('子时 23:00-01:00：1 ')
    print('丑时 01:00-03:00：2 ')
    print('寅时 03:00-05:00：3 ')
    print('卯时 05:00-07:00：4 ')
    print('辰时 07:00-09:00：5 ')
    print('巳时 09:00-11:00：6 ')
    print('午时 11:00-13:00：7 ')
    print('未时 13:00-15:00：8 ')
    print('申时 15:00-17:00：9 ')
    print('酉时 17:00-19:00：10')
    print('戌时 19:00-21:00：11')
    print('亥时 21:00-23:00：12','\n')

def YunSuan():
    #六神定义
    dict_list = ['大安','留连','速喜','赤口','小吉','空亡']
    dict_key = ['大安','留连','速喜','赤口','小吉','空亡']
    dict ={"大安":Daan,'留连':LiuLian,'速喜':SuXi,'赤口':ChiKou,'小吉':XiaoJi,'空亡':KongWang}
    s_month = int(input("请输入月/随机数："))
    s_day = int(input("请输入日/随机数："))
    s_hour = int(input("请输入时辰："))

    # 运算 推算日月时辰对应的数字
    sum = s_month + s_day - 1
    today_i = int((sum - 1) % 6)
    month_i = int((s_month - 1) % 6)
    hour = s_month + s_day + s_hour
    hour_i =int((hour - 3) % 6)


    #运算 年月时辰对应的 六神三宫
    today_f = dict_list[today_i]
    month_f = dict_list[month_i]
    hour_f = dict_list[hour_i]
    print('三宫所属：',month_f,'☯',today_f,'☯',hour_f +'\n')
    today_o = dict[dict_key[today_i]]()
    month_o = dict[dict_key[month_i]]()
    hour_o = dict[dict_key[hour_i]]()
    print(month_o+'\n\n',today_o+'\n\n',hour_o)
    print(HeGong())



if __name__ == '__main__':
    ShiChen()
    YunSuan()



# Python 3.8.8
# -*- Coding: UTF-8 -*-
# CreateDate: 2023-10-18 12:53
# Author: wuhulamb
import sys
import os
import re
import datetime
import numpy as np
import pandas as pd

print(r'''
       __      __                              __                     
  ____/ /___ _/ /_____ _      ____ ___  ____ _/ /_____    ____  __  __
 / __  / __ `/ __/ __ `/_____/ __ `__ \/ __ `/ //_/ _ \  / __ \/ / / /
/ /_/ / /_/ / /_/ /_/ /_____/ / / / / / /_/ / ,< /  __/ / /_/ / /_/ / 
\__,_/\__,_/\__/\__,_/     /_/ /_/ /_/\__,_/_/|_|\___(_) .___/\__, /  
                                                      /_/    /____/                  
                                 _        _           
             _ __ ___   __ _  __| | ___  | |__  _   _ 
            | '_ ` _ \ / _` |/ _` |/ _ \ | '_ \| | | |
            | | | | | | (_| | (_| |  __/ | |_) | |_| |
            |_| |_| |_|\__,_|\__,_|\___| |_.__/ \__, |
                                                |___/ 
                    __               ___                        __        
                   /\ \             /\_ \                      /\ \       
 __  __  __  __  __\ \ \___   __  __\//\ \      __      ___ ___\ \ \____  
/\ \/\ \/\ \/\ \/\ \\ \  _ `\/\ \/\ \ \ \ \   /'__`\  /' __` __`\ \ '__`\ 
\ \ \_/ \_/ \ \ \_\ \\ \ \ \ \ \ \_\ \ \_\ \_/\ \L\.\_/\ \/\ \/\ \ \ \L\ \
 \ \___x___/'\ \____/ \ \_\ \_\ \____/ /\____\ \__/.\_\ \_\ \_\ \_\ \_,__/
  \/__//__/   \/___/   \/_/\/_/\/___/  \/____/\/__/\/_/\/_/\/_/\/_/\/___/ 

''')


def tozero(m: int, d: int, y: int):
    """
    计算输入日期到数学0年（公元元年1月1日前一天）的天数
    """
    normal_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    # 闰年 四年一闰 百年不闰 四百年一闰 1900不是闰年 2000是闰年 2020是闰年
    n = (y - 1) // 100
    q = (y - 1) // 4 - (n - (n // 4))  # 从输入日期的前一年到数学0年的闰年数
    a = q * 366 + (y - 1 - q) * 365    # 从输入日期的前一年到数学0年的天数
    if m > 1:  # 对月的情况进行讨论
        if (y % 100 != 0 and y % 4 == 0) or (y % 100 == 0 and y % 400 == 0):  # 闰年的情况
            b = sum([leap_year[z] for z in range(1, m)])                      # b是m之前月份的天数和
        else:                                                                 # 平年的情况
            b = sum([normal_year[z] for z in range(1, m)])
    else:
        b = 0
    return a + b + d

def yesterday(m: int, d: int, y: int):
    """
    返回输入日期前一天是几月几号
    """
    normal_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if m > 1:  # 对月的情况进行讨论
        lastm = m - 1
        lasty = y
        if (y % 100 != 0 and y % 4 == 0) or (y % 100 == 0 and y % 400 == 0):  # 闰年的情况
            lastd = leap_year[lastm]
        else:                                                                 # 平年的情况
            lastd = normal_year[lastm]
    else:
        lastm = 12
        lastd = 31
        lasty = y - 1
    if d > 1:
        return (m, d - 1, y)
    else:
        return (lastm, lastd, lasty)

# t % 7 {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
def weekday(m: int, d: int, y: int):
    """
    返回输入日期是星期几
    """
    return tozero(m, d, y) % 7

# 计算第几周
def whichweek(m: int, d: int, y: int, week1m, week1d, week1y):  # week1m, week1d为第一周的第一天（礼拜一的前一天————周日）
    """
    返回输入日期所在周次（如第一周）
    """
    t = tozero(m, d, y) - tozero(week1m, week1d, week1y)
    return t // 7 + 1


# 一些重要的默认值
crtyear = 2024                        # 当前的年份
week1m, week1d, week1y = 2, 25, 2024  # 当前学期的第一周的第一天

m, d, y = datetime.date.today().strftime('%m-%d-%Y').split('-')
m, d, y = int(m), int(d), int(y)
# m, d, y = 4, 7, 2024                                      # 正式投入使用时请注释本行|与星期需匹配
if tozero(m, d, y) - tozero(week1m, week1d, week1y) > 150:  # 150 是用来提醒新学期重新配置相关参数
    print('请更新程序中开学第一周第一天的具体日期')
    sys.exit(1)

x = input("[-] 处理闻韶楼，请输1\n[-] 处理天山堂/秦岭堂，请输2\n[-] 退出程序，请输0\n[*] 在此处输入：")
if x == '1':
    data = {}
    data["序号"] = []
    data["课程名称"] = []
    data["开课院系"] = []
    data["课程号"] = []
    data["课序号"] = []
    data["选课人数"] = []
    data["选课属性"] = []
    data["主讲教师姓名"] = []
    data["主讲教师所在院系"] = []
    data["合讲教师"] = []
    data["合班"] = []
    data["周次分布"] = []
    data["具体日期"] = []
    data["星期"] = []
    data["节次"] = []
    data["教室"] = []
    data["教师是否正常到课"] = []
    data["学生是否正常到课"] = []
    data["备注"] = []
    hdr_data = {}
    yesterdayNum = 0
    todayNum = 0
    
    print('''
    [NOTICE]
    * 原始到课数据的条数一定要保证无误
    * 办公室助理异常表需删除上周五的课程（保证全是本周课程）
    * 文件路径输入不能有引号、空格
    * 按Ctrl+C即可中断程序
    ''')
    check_pth = input('请输入闻韶楼数据表（表头+内容）：')
    office_pth = input('请输入办公室助理的异常表：')
    save_pth = input(r'请输入生成文件路径（eg. D:\xxx\xxx，按回车直接生成在程序所在文件夹）：')

    check_pth = '/'.join(check_pth.split('\\'))
    office_pth = '/'.join(office_pth.split('\\'))

    lastm, lastd, lasty = yesterday(m, d, y)
    weekToday = weekday(m, d, y)
    weekYesterday = weekday(lastm, lastd, lasty)


    print('\n到课率表：\n')
    # print("【出现报错】（problem['教室情况（详细阐述）'].append(info_data.strip())）\n则数据表里查课同学无备注but异常表办公室助理有备注\n")
    wb_check = pd.read_excel(check_pth, header=None)     # 表头+当天需要处理的数据
    wb_office = pd.read_excel(office_pth, header=None)
    issue = {}
    hdr_issue = {}
    for k, foo in enumerate(wb_office.values[1]):
        if k < 14:
            hdr_issue[k] = foo
            issue[foo] = []
    for i in wb_office.values[2:]:
        for k, j in enumerate(i):
            if k < 14:
                issue[hdr_issue[k]].append(str(j))
    issue_df = pd.DataFrame(issue)

    for k, foo in enumerate(wb_check.values[0]):
        hdr_data[k] = foo
    for i in wb_check.values[1:]:
        # 从一行数据中逐个提取需要的信息
        for k, j in enumerate(i):
            if hdr_data[k] == '选课人数':            # int
                selhum = int(j)
                data[hdr_data[k]].append(selhum)
            if hdr_data[k] == '星期':                # str
                week_data = str(j)
                data[hdr_data[k]].append(week_data)
            if hdr_data[k] == '节次':                # str
                classNum_data = j
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '教室':                # str
                classroom_data = j
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '合班':                # str/nan
                stu_class = j
                data[hdr_data[k]].append(j)
            # 不做处理的信息
            if hdr_data[k] == '课程名称':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '开课院系':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '课程号':
                data[hdr_data[k]].append(str(j))
            if hdr_data[k] == '课序号':
                data[hdr_data[k]].append(str(j))
            if hdr_data[k] == '选课属性':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '主讲教师姓名':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '主讲教师所在院系':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '合讲教师':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '周次分布':
                data[hdr_data[k]].append(j)
        
        # 根据星期计算具体日期并填入，同时填入序号
        if week_data == str(weekYesterday):
            yesterdayNum += 1
            data['具体日期'].append('%.2d.%.2d' %(lastm, lastd))
            data['序号'].append(yesterdayNum)
        elif week_data == str(weekToday):
            todayNum += 1
            data['具体日期'].append('%.2d.%.2d' %(m, d))
            data['序号'].append(todayNum)
        else:
            print('日期与星期不匹配')
        
        # 写入异常情况备注
        for bar in issue_df[(issue_df['星期'] == str(weekYesterday)) | (issue_df['星期'] == str(weekToday))].values:
            # 从一行数据中依次提取相关信息
            for k, foo in enumerate(bar):
                if hdr_issue[k] == '星期':     # str
                    week_iss = foo.strip()     # 去前后空格，减少人为错误导致程序出现error
                if hdr_issue[k] == '节次':     # str
                    classNum_iss = foo.strip()
                if hdr_issue[k] == '教室':     # str
                    classroom_iss = foo.strip()
                if hdr_issue[k] == '备注信息':  # str
                    info_iss = foo.strip()
            if '闻韶楼' in classroom_iss or '美术' in classroom_iss or '音乐' in classroom_iss:
                if '闻韶楼' in classroom_iss:
                    classroom_iss = classroom_iss[3:].upper()
                else:
                    classroom_iss = classroom_iss.upper()
                # print(f'{week_data} == {week_iss} & {classNum_data} == {classNum_iss} & {classroom_data} == {classroom_iss}')
                if week_data == week_iss and classNum_data == classNum_iss and classroom_data == classroom_iss:
                    comment = info_iss
                    print(f'【闻韶楼到课异常（备注已写入到课表）】星期{week_data} {classNum_data} {classroom_data} 课程：{data["课程名称"][-1]} 备注：{comment}\n')
                    break
        else:
            comment = ''                      # 办公室助理无备注
        if comment == '':
            data['教师是否正常到课'].append('Y')
            data['学生是否正常到课'].append('Y')
        else:
            data['教师是否正常到课'].append('N')
            data['学生是否正常到课'].append('N')

        data['备注'].append(comment)

    # 提取待做数据的各时间段及教室，为后续遍历找到合班做准备
    data_df = pd.DataFrame(data)
    if save_pth == '':
        data_df.to_excel('闻韶楼%d月%d日学生到课情况统计表.xlsx' %(m, d), index=False)
    else:
        save_pth = '/'.join(save_pth.split('\\'))
        data_df.to_excel('%s/闻韶楼%d月%d日学生到课情况统计表.xlsx' %(save_pth, m, d), index=False)
    
    print('只是打印输出昨天、今天的闻韶楼异常以作检查之用：')
    for bar in issue_df[(issue_df['星期'] == str(weekYesterday)) | (issue_df['星期'] == str(weekToday))].values:
        # 从一行数据中依次提取相关信息
        for k, foo in enumerate(bar):
            if hdr_issue[k] == '星期':     # str
                week_iss = foo.strip()     # 去前后空格，减少人为错误导致程序出现error
            if hdr_issue[k] == '节次':     # str
                classNum_iss = foo.strip()
            if hdr_issue[k] == '教室':     # str
                classroom_iss = foo.strip()
            if hdr_issue[k] == '备注信息':  # str
                info_iss = foo.strip()
            if hdr_issue[k] == '课程名称':  # str
                name = foo.strip()
        if '闻韶楼' in classroom_iss or '美术' in classroom_iss or '音乐' in classroom_iss:    # 异常表中找到闻韶楼
            print(f'【闻韶楼到课异常】星期{week_iss} {classNum_iss} {classroom_iss} 课程：{name} 备注：{info_iss}\n')
    weekNum2Str = {1: "第一周", 2: "第二周", 3: "第三周", 4: "第四周", 5: "第五周", 6: "第六周", 7: "第七周", 8: "第八周", 9: "第九周", 10: "第十周", 11: "第十一周", 12: "第十二周", 13: "第十三周", 14: "第十四周", 15: "第十五周", 16: "第十六周", 17: "第十七周", 18: "第十八周", 19: "第十九周", 20: "第二十周",}               
    print(f'''
    【到课表注意事项】
    1. 调课至不同时段的备注需改成具体日期（其他备注也根据需要进行调整，如删除nan）
    2. 添加：X月X日闻韶楼第X-X节到课情况统计表（{weekNum2Str[whichweek(m, d, y, week1m, week1d, week1y)]}周X）
    3. 无师生的情况标黄
    4. 字体、字号、行高、列宽、边框
    5. 添加最后一行的备注说明
    ''')

elif x == '2':
    data = {}
    data["序号"] = []
    data["课程名称"] = []
    data["开课院系"] = []
    data["课程号"] = []
    data["课序号"] = []
    data["选课人数"] = []
    data["选课属性"] = []
    data["主讲教师姓名"] = []
    data["主讲教师所在院系"] = []
    data["合讲教师"] = []
    data["合班"] = []
    data["周次分布"] = []
    data["具体日期"] = []
    data["星期"] = []
    data["节次"] = []
    data["教室"] = []
    data["到课人数"] = []
    data["到课率"] = []
    data["备注"] = []
    hdr_data = {}
    yesterdayNum = 0
    todayNum = 0
    day = []
    classTime = []
    classRoom = []
    problemNum = 0
    problem = {}
    problem["序号"] = []
    problem["课程名称"] = []
    problem["开课院系"] = []
    problem["课程号"] = []
    problem["课序号"] = []
    problem["主讲教师姓名"] = []
    problem["周次分布"] = []
    problem["具体周次"] = []
    problem["星期"] = []
    problem["节次"] = []
    problem["教室"] = []
    problem["选课人数"] = []
    problem["实到人数"] = []   # 原到课人数
    problem["教室情况（详细阐述）"] = []
    problem["截图名称"] = []
    problem["核实情况"] = []

    def problem_fill(num):
        problem['序号'].append(num)
        problem['课程名称'].append(data['课程名称'][-1])
        problem['开课院系'].append(data['开课院系'][-1])
        problem['课程号'].append(data['课程号'][-1])
        problem['课序号'].append(data['课序号'][-1])
        problem['主讲教师姓名'].append(data['主讲教师姓名'][-1])
        problem['周次分布'].append(data['周次分布'][-1])
        problem['具体周次'].append(whichweek(m, d, y, week1m, week1d, week1y))
        problem['星期'].append(data['星期'][-1])
        problem['节次'].append(data['节次'][-1])
        problem['教室'].append(data['教室'][-1])
        problem['选课人数'].append(data['选课人数'][-1])
        problem['实到人数'].append(data['到课人数'][-1])
        problem['截图名称'].append('%.4d%.2d%.2d%s截图%d' %(y, m, d, place, num))

    print('''
    [NOTICE]
     * 原始到课数据的条数一定要保证无误
     * 办公室助理异常表需删除上周五的课程（保证全是本周课程）
     * 截图文件夹里的节次文件夹名需保证正确（有时会出现奇怪数字字母）
     * 文件路径输入不能有引号、空格
     * 按Ctrl+C即可中断程序
    ''')
    place = input('请输入做数据地点（天山堂/秦岭堂）：')
    check_pth = input('请输入今天要做的数据表（表头+内容）：')
    office_pth = input('请输入办公室助理的异常表：')
    picture_pth = input(r'请输入截图文件夹路径（eg. D:\xxx\xxx 【第x周上一层】 OR n【不输入截图】）：')
    save_pth = input(r'请输入生成文件路径（eg. D:\xxx\xxx，按回车直接生成在当前工作路径）：')

    check_pth = '/'.join(check_pth.split('\\'))
    office_pth = '/'.join(office_pth.split('\\'))

    lastm, lastd, lasty = yesterday(m, d, y)
    weekToday = weekday(m, d, y)
    weekYesterday = weekday(lastm, lastd, lasty)

    weekday2str = {0: "周日", 1: "周一", 2: "周二", 3: "周三", 4: "周四", 5: "周五", 6: "周六"}
    weekNum2Str = {1: "第一周", 2: "第二周", 3: "第三周", 4: "第四周", 5: "第五周", 6: "第六周", 7: "第七周", 8: "第八周", 9: "第九周", 10: "第十周", 11: "第十一周", 12: "第十二周", 13: "第十三周", 14: "第十四周", 15: "第十五周", 16: "第十六周", 17: "第十七周", 18: "第十八周", 19: "第十九周", 20: "第二十周",}
    
    print('\n到课率表+异常表：\n')
    # print("【出现报错】（problem['教室情况（详细阐述）'].append(info_data.strip())）\n则数据表里查课同学无备注but异常表办公室助理有备注\n")
    wb_check = pd.read_excel(check_pth, header=None)     # 表头+当天需要处理的数据
    wb_office = pd.read_excel(office_pth, header=None)

    issue = {}
    hdr_issue = {}   # 办公室助理异常表
    for k, foo in enumerate(wb_office.values[1]):
        if k < 14:
            hdr_issue[k] = foo
            issue[foo] = []
    for i in wb_office.values[2:]:
        for k, j in enumerate(i):
            if k < 14:
                issue[hdr_issue[k]].append(str(j))
    issue_df = pd.DataFrame(issue)

    for k, foo in enumerate(wb_check.values[0]):
        hdr_data[k] = foo
    for i in wb_check.values[1:]:
        maxhum = 0
        # 从一行数据中逐个提取需要的信息
        for k, j in enumerate(i):
            if hdr_data[k] == '到课人数':            # int
                if not np.isnan(j) and maxhum < int(j):
                    maxhum = int(j)
            if hdr_data[k] == '选课人数':            # int
                selhum = int(j)
                data[hdr_data[k]].append(selhum)
            if hdr_data[k] == '星期':                # str
                week_data = str(j)
                day.append(week_data)
                data[hdr_data[k]].append(week_data)
            if hdr_data[k] == '节次':                # str
                classNum_data = j
                classTime.append(j)
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '教室':                # str
                classroom_data = j
                classRoom.append(j)
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '合班':                # str/nan
                stu_class = j
                data[hdr_data[k]].append(j)
            # 不做处理的信息
            if hdr_data[k] == '课程名称':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '开课院系':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '课程号':
                data[hdr_data[k]].append(str(j))
            if hdr_data[k] == '课序号':
                data[hdr_data[k]].append(str(j))
            if hdr_data[k] == '选课属性':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '主讲教师姓名':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '主讲教师所在院系':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '合讲教师':
                data[hdr_data[k]].append(j)
            if hdr_data[k] == '周次分布':
                data[hdr_data[k]].append(j)


            if k == 22:                              # info_data查课同学备注，如果表头更改此处也需要更改
                info_data = j
        data['到课人数'].append(maxhum)               # int
        if maxhum / selhum > 1:                      # 到课率超过1改为1
            data['到课率'].append(1.0)
        else:
            data['到课率'].append(maxhum / selhum)    # float
        
        # 根据星期计算具体日期并填入，同时填入序号
        if week_data == str(weekYesterday):
            yesterdayNum += 1
            data['具体日期'].append('%.2d.%.2d' %(lastm, lastd))
            data['序号'].append(yesterdayNum)
        elif week_data == str(weekToday):
            todayNum += 1
            data['具体日期'].append('%.2d.%.2d' %(m, d))
            data['序号'].append(todayNum)
        else:
            print('日期与星期不匹配')

        # 写入异常情况备注
        for bar in issue_df[(issue_df['星期'] == str(weekYesterday)) | (issue_df['星期'] == str(weekToday))].values:
            # 从一行数据中依次提取相关信息
            for k, foo in enumerate(bar):
                if hdr_issue[k] == '星期':     # str
                    week_iss = foo.strip()     # 去前后空格，减少人为错误导致程序出现error
                if hdr_issue[k] == '节次':     # str
                    classNum_iss = foo.strip()
                if hdr_issue[k] == '教室':     # str
                    classroom_iss = foo.strip()
                if hdr_issue[k] == '备注信息':  # str
                    info_iss = foo.strip()
            if place in classroom_iss:
                if place == '天山堂':
                    classroom_iss = classroom_iss[3:].upper()
                else:
                    classroom_iss = classroom_iss.upper()
                # print(f'{week_data} == {week_iss} & {classNum_data} == {classNum_iss} & {classroom_data} == {classroom_iss}')
                if week_data == week_iss and classNum_data == classNum_iss and classroom_data == classroom_iss:
                    comment = info_iss
                    if data['到课率'][-1] < 0.7 or '老师迟到' in comment:
                        if isinstance(info_data, str):         # 正常情况
                            info_data = info_data.strip()
                        else:                                  # 办公室助理有记录but查课同学无备注
                            print(f'【办公室助理有备注but查课同学无备注（或备注错列了），备注已写入到课率表+异常表】 星期{week_data} {classNum_data} {classroom_data} 课程：{data["课程名称"][-1]} 办公室备注：{comment}\n')
                        problemNum += 1
                        problem_fill(problemNum)
                        problem['教室情况（详细阐述）'].append(info_data)
                        problem['核实情况'].append(comment)
                        try:
                            if '老师迟到' in comment or '老师迟到' in info_data:
                                print(f'\n【老师迟到】 星期{week_data} {classNum_data} {classroom_data} 课程：{data["课程名称"][-1]}\n')
                        except:
                            pass
                    break
        else:
            comment = ''                      # 办公室助理无备注
        if comment == '':                     # 办公室助理无备注
            if 0 < data['到课率'][-1] < 0.7:
                # 数据处理 增加辅修备注
                if isinstance(stu_class, str) and '辅修' in stu_class:
                    comment = '双学位课程，部分学生课程冲突'

                # 数据处理 增加大四学生备注
                # if isinstance(stu_class, str) and old_grade in stu_class:
                #     comment = '大四学生，找工作较多'

            if isinstance(info_data, str):     # 查课同学有备注
                info_data = info_data.strip()
                if data['到课率'][-1] < 0.7 or '老师迟到' in info_data:
                    problemNum += 1
                    problem_fill(problemNum)
                    problem['教室情况（详细阐述）'].append(info_data)
                    problem['核实情况'].append(comment)
                    if '老师迟到' in info_data:
                        print(f'\n【老师迟到】 星期{week_data} {classNum_data} {classroom_data} 课程：{data["课程名称"][-1]}\n')
                else:
                    print(f'\n【到课率正常，未写入异常表，注意查课同学备注】星期{week_data} {classNum_data} {classroom_data} 课程：{data["课程名称"][-1]} 查课同学备注：{info_data}\n')
                if info_data not in ['到课率不足70%', '到课率低于70%', '到课率小于70%']:
                    comment = info_data
                    print('【查课同学有备注but办公室助理无备注，请人工核查（到课表中已写入该备注，如果是类似到课率·不足·70%，需检查是否要改为辅修）】')
                    print(f'星期{week_data} {classNum_data} {classroom_data} 课程：{data["课程名称"][-1]} 查课同学备注：{info_data}（可根据查课同学备注筛选）\n')
            else:
                if 0 < data['到课率'][-1] < 0.7:
                    problemNum += 1
                    problem_fill(problemNum)
                    problem['教室情况（详细阐述）'].append('到课率不足70%')
                    problem['核实情况'].append(comment)
                    print('【到课率低于70%，查课同学无备注，程序已写入异常情况表中】')
                    print('星期%s 新表序号%d 课程名称：%s 到课率%.2f\n' %(week_data, data['序号'][-1], data['课程名称'][-1], data['到课率'][-1]))
                elif data['到课率'][-1] == 0:
                    print('【严重问题，到课率为0%，办公室助理无备注and查课同学无备注，请核实情况】')
                    print(f'星期{week_data} {classNum_data} {classroom_data} 课程：{data["课程名称"][-1]} 查课同学备注：{info_data}\n')
                else:
                    pass
                
        data['备注'].append(comment)

    # 提取待做数据的各时间段及教室，为后续遍历找到合班做准备
    day = set(day)
    classTime = set(classTime)
    classRoom = set(classRoom)
    data_df = pd.DataFrame(data)
    problem_df = pd.DataFrame(problem)

    hdr_data_df = {}   # 表头:列序号 这样就算改变到课率结构 也不会影响后面合班问题修正
    for k, foo in enumerate(data_df.columns.values):
        hdr_data_df[foo] = k
    # 合班问题修正
    print('\n合班问题修正：')
    for _ in day:
        for i in classTime:
            for j in classRoom:
                special = data_df[(data_df['星期'] == _) & (data_df['节次'] == i) & (data_df['教室'] == j)]
                if len(special) > 1:
                    tosum = [k for k in special["到课人数"].values]
                    temp = set(tosum)
                    if len(temp) > 1:
                        gap = max(temp) - min(temp)
                        if gap > 5:
                            right_rate = sum(tosum) / sum([int(p) for p in special["选课人数"].values])
                            if right_rate > 1:
                                right_rate = 1
                                print(f'合班到课率超过1，已重新赋值为1：')
                            for t in special.values:
                                if abs(right_rate - t[hdr_data_df['到课率']]) > 0.0001:
                                    data_df.loc[(data_df['序号'] == t[hdr_data_df['序号']]) & (data_df['具体日期'] == t[hdr_data_df['具体日期']]), '到课率'] = right_rate
                                    print(f'【合班（到课率已修正）| 查课同学记录多个值and不同值差别大】 序号{t[hdr_data_df["序号"]]} {t[hdr_data_df["具体日期"]]} {t[hdr_data_df["节次"]]} {t[hdr_data_df["教室"]]} 选课{t[hdr_data_df["选课人数"]]} 到课{t[hdr_data_df["到课人数"]]} 合到课率{right_rate} 课程：{t[hdr_data_df["课程名称"]]}')
                                else:
                                    print(f'【合班（合到课率=分到课率）| 查课同学记录多个值and不同值差别大】 序号{t[hdr_data_df["序号"]]} {t[hdr_data_df["具体日期"]]} {t[hdr_data_df["节次"]]} {t[hdr_data_df["教室"]]} 选课{t[hdr_data_df["选课人数"]]} 到课{t[hdr_data_df["到课人数"]]} 合到课率{right_rate} 课程：{t[hdr_data_df["课程名称"]]}')
                        else:
                            right_rate = max(tosum) / sum([int(p) for p in special["选课人数"].values])
                            if right_rate > 1:
                                right_rate = 1
                                print('合班到课率超过1，已重新赋值为1：')
                            for t in special.values:
                                if abs(right_rate - t[hdr_data_df['到课率']]) > 0.0001:
                                    data_df.loc[(data_df['序号'] == t[hdr_data_df['序号']]) & (data_df['具体日期'] == t[hdr_data_df['具体日期']]), '到课率'] = right_rate
                                    print(f'【合班（到课率已修正）| 查课同学记录多个值and不同值差别小】 序号{t[hdr_data_df["序号"]]} {t[hdr_data_df["具体日期"]]} {t[hdr_data_df["节次"]]} {t[hdr_data_df["教室"]]} 选课{t[hdr_data_df["选课人数"]]} 到课{t[hdr_data_df["到课人数"]]} 合到课率{right_rate} 课程：{t[hdr_data_df["课程名称"]]}')
                                else:
                                    print(f'【合班（合到课率=分到课率）| 查课同学记录多个值and不同值差别小】 序号{t[hdr_data_df["序号"]]} {t[hdr_data_df["具体日期"]]} {t[hdr_data_df["节次"]]} {t[hdr_data_df["教室"]]} 选课{t[hdr_data_df["选课人数"]]} 到课{t[hdr_data_df["到课人数"]]} 合到课率{right_rate} 课程：{t[hdr_data_df["课程名称"]]}')
                        #for t in special.values:
                        #    print('【合班，查课同学记录多个值，到课表中未更改】')
                        #    print(f'序号{t[0]} {t[11]} {t[13]} {t[14]} 课程：{t[1]} 选课{t[4]} 到课{t[15]}\n')
                    else:
                        right_rate = special["到课人数"].values[0] / sum([int(p) for p in special["选课人数"].values])
                        if right_rate > 1:
                                right_rate = 1
                                print('合班到课率超过1，已重新赋值为1：')
                        for t in special.values:
                            if abs(right_rate - t[hdr_data_df['到课率']]) > 0.0001:
                                # print(f'{place} 合班问题 正确到课率：{right_rate}')
                                # print(f'序号{t[0]} 日期{t[11]} 节次{t[13]} 教室{t[14]} 开课院系{t[2]} 课程{t[1]} 选课{t[4]} 到课{t[15]} 原到课率{t[16]}')
                                data_df.loc[(data_df['序号'] == t[hdr_data_df['序号']]) & (data_df['具体日期'] == t[hdr_data_df['具体日期']]), '到课率'] = right_rate
                                print(f'【合班（到课率已修正）| 查课同学记录一个值】 序号{t[hdr_data_df["序号"]]} {t[hdr_data_df["具体日期"]]} {t[hdr_data_df["节次"]]} {t[hdr_data_df["教室"]]} 选课{t[hdr_data_df["选课人数"]]} 到课{t[hdr_data_df["到课人数"]]} 合到课率{right_rate} 课程：{t[hdr_data_df["课程名称"]]}')
                            else:
                                print(f'【合班（合到课率=分到课率）| 查课同学记录一个值】 序号{t[hdr_data_df["序号"]]} {t[hdr_data_df["具体日期"]]} {t[hdr_data_df["节次"]]} {t[hdr_data_df["教室"]]} 选课{t[hdr_data_df["选课人数"]]} 到课{t[hdr_data_df["到课人数"]]} 合到课率{right_rate} 课程：{t[hdr_data_df["课程名称"]]}')

    if save_pth == '':
        os.makedirs('%04d%02d%02d%s/%d月%d日榆中校区截图' %(y, m, d, place, m, d))
        data_df.to_excel('%04d%02d%02d%s/%s%d月%d日学生到课情况统计表.xlsx' %(y, m, d, place, place, m, d), index=False)
        problem_df.to_excel('%04d%02d%02d%s/%d月%d日榆中校区截图/%s2023秋季学期异常课堂截图记录（%04d%02d%02d）.xlsx' %(y, m, d, place, m, d, place, y, m, d), index=False)               # 每学期改一下异常表名称的时间（2023秋）
    else:
        save_pth = '/'.join(save_pth.split('\\'))
        os.makedirs('%s/%04d%02d%02d%s/%d月%d日榆中校区截图' %(save_pth, y, m, d, place, m, d))
        data_df.to_excel('%s/%04d%02d%02d%s/%s%d月%d日学生到课情况统计表.xlsx' %(save_pth, y, m, d, place, place, m, d), index=False)
        problem_df.to_excel('%s/%04d%02d%02d%s/%d月%d日榆中校区截图/%s2023秋季学期异常课堂截图记录（%04d%02d%02d）.xlsx' %(save_pth, y, m, d, place, m, d, place, y, m, d), index=False)  # 每学期改一下异常表名称的时间（2023秋）

    print(f'''
    【到课表注意事项】
    1. 到课率需要将格式调为%，并保留两位小数
    2. 到课率为0的四史课是否为线上授课
    3. 备注调整：调课至不同时段的备注需改成具体日期（其他如删除nan/老师迟到/到课率小于70%）
    4. 添加：X月X日{place}第X-X节到课情况统计表（{weekNum2Str[whichweek(m, d, y, week1m, week1d, week1y)]}周X）
    5. 到课率低于70%标黄
    6. 字体、字号、行高、列宽、边框
    7. 添加最后一行的备注说明
    ''')
    
    # 截图命名
    if picture_pth == 'n':
        print('\n无截图文件输入\n')
    else:
        print('\n截图：\n')
        picture_pth = '/'.join(picture_pth.split('\\'))
        for i in problem_df[['课程名称', '具体周次', '星期', '节次', '教室', '截图名称']].values:
            classn = i[3]
            classn_os = os.listdir('%s/第%d周/%s' %(picture_pth, i[1], weekday2str[int(i[2])]))            # 第3周
            if classn == '9-10节':
                classn = '9-11节'
            if classn not in classn_os:
                print(f'【异常课程的节次{i[3]}，不在截图文件夹中】{i[5]} 星期{i[2]} {i[3]} {i[4]} 课程：{i[0]}\n')
            else:
                pics = os.listdir('%s/第%d周/%s/%s' %(picture_pth, i[1], weekday2str[int(i[2])], classn))  # 第3周
                pics = [p.upper() for p in pics]                                                       # windows系统不区分大小写，所以可以这样，linux不行
                classroom_num = re.search('.*?([a-zA-Z][0-9]{3}).*', i[4]).group(1).upper() + '.JPG'   # 去除文字，只留教室号
                if classroom_num in pics:
                    with open('%s/第%d周/%s/%s/%s' %(picture_pth, i[1], weekday2str[int(i[2])], classn, classroom_num), 'rb') as fp:
                        if save_pth == '':
                            with open('%04d%02d%02d%s/%d月%d日榆中校区截图/%s.JPG' %(y, m, d, place, m, d, i[5]), 'wb') as ft:
                                ft.write(fp.read())
                        else:
                            with open('%s/%04d%02d%02d%s/%d月%d日榆中校区截图/%s.JPG' %(save_pth, y, m, d, place, m, d, i[5]), 'wb') as ft:
                                ft.write(fp.read())
                else:
                    print(f'{classroom_num} NOT in {pics} 课程：{i[0]} 星期{i[2]} {i[3]}')

else:
    print('输入的是0或者其他，程序已退出')
    sys.exit(1)

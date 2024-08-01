---
title:            "每日到课率整理@Python"
author:           "wuhulamb"
date:             "2023-11-02 18:53:00 +0800"
last_modified_at: "2024-04-27 14:00:00 +0800"
categories:
  - "技术应用"
tags:
  - "教务处勤工助学"
  - "Python"
header:
  overlay_image:           "assets/hero-img/posts/city-night.jpg"
---

> 在~~询问作者~~使用程序前，请仔细阅读本教程，90%的问题都可以在这里找到答案！

## 写给谁

- 需要使用该程序进行数据处理的小伙伴<!--more-->
- ~~想要了解技术实现思路的人（先留一个坑，以后有空再填）~~

## 功能

- 制作每日到课率表
- 制作异常情况表 + 截图重命名

## 程序下载

点击 :point_right: [data-make.py]({{ 'media/download/data-make.py' | relative_url }}) 下载使用

**Note:** 本代码使用的 `Python` 版本为 `3.8.8` （请保证使用的 `Python` 版本至少是 `3.0.0` 之后），且需要安装 `numpy` 和 `pandas` 两个库
{: .notice--info}

```text
python -m pip install numpy
python -m pip install pandas
```

**Warn:** 每学期需要更新代码中 `crtyear` 、 `week1m` 、 `week1d` 、 `week1y` 参数值
{: .notice--warning}

## 开始使用

### 1. 数据准备

#### （1）目录结构示例

说明：备注【命名】则是需要确保**文件或文件夹名称**符合示例要求

```text
.
├── 第7周异常情况记录备案.xlsx     # 确保异常记录都是本周的即可（如果没有异常，则准备一个没有内容，只有大表头和小表头的表）
├── 闻韶楼.xlsx                   # 确保数据在第一个sheet里
├── 天山堂                        # 文件夹
│   ├── 天山堂.xlsx               # 确保数据在第一个sheet里
│   └── 第7周                     # 【命名】第7周√，第七周×
│       ├── 周一                  # 【命名】昨天的截图（必需包含9-11节，可以多不能少，为了方便通常整个复制过来；如果是周一就只留周一的截图即可）
│       │   ├── 1-2节             # 【命名】
│       │   │   ├── A302.JPG      # A302-1.JPG无法识别，需手动移动到相应文件夹（程序会根据异常情况主动搜索相应JPG，未找到的会打印输出提示出来）
│       │   │   └── B401.JPG
│       │   ├── 3-4节             # 【命名】
│       │   ├── 5-6节             # 【命名】
│       │   ├── 7-8节             # 【命名】
│       │   └── 9-11节            # 【命名】
│       └── 周二                  # 【命名】今天的截图，目录结构同周一（可以多不能少，例如可以有晚上9-11节的截图）
└── 秦岭堂                        # 目录结构同天山堂
```

截图示例（**./** 表示当前目录，使用相对路径）

| 路径示例 | 路径示例 |
| :---: | :---: |
| ![data-env1.png]({{ 'media/image/2023/11/data-env1.png' | relative_url }} "environment") **./** | ![data-env2.png]({{ 'media/image/2023/11/data-env2.png' | relative_url }} "environment") **./天山堂/** |
| ![data-env3.png]({{ 'media/image/2023/11/data-env3.png' | relative_url }} "environment") **./天山堂/第7周/** | ![data-env4.png]({{ 'media/image/2023/11/data-env4.png' | relative_url }} "environment") **./天山堂/第7周/周二/** |
| ![data-env5.png]({{ 'media/image/2023/11/data-env5.png' | relative_url }} "environment") **./天山堂/第7周/周二/7-8节/** |

#### （2）到课率原始数据【查课助理】

只保留**小表头** + **今天要处理的数据**（eg. 周二9-11+周三1-8），建议**按行复制**，不要遗漏备注，最后另存为新表，数据存入**新表的第一个sheet**中

![original-data.png]({{ 'media/image/2023/11/original-data.png' | relative_url }})  
*此处以秦岭堂为例，天山堂、闻韶楼同理*

#### （3）异常情况记录备案【办公室助理】

如果有**上周周5**异常课程的记录，**需删除**（删除后序号无需调整），保证记录的异常情况都是本周的，其余不变

![office.png]({{ 'media/image/2023/11/office.png' | relative_url }})

#### （4）截图

截图路径示例（注意：截图存放在**第7周**，不是第七周）

```text
F:\到课情况原始数据\20231017\天山堂   #「第7周」文件夹上一级
```

![data-env2.png]({{ 'media/image/2023/11/data-env2.png' | relative_url }} "environment")

### 2. 运行程序

#### （1）打开cmd

![cmd.png]({{ 'media/image/2023/11/cmd.png' | relative_url }} "cmd")

#### （2）运行程序

```text
python .\data-make.py  # 运行程序
```

![data-make.png]({{ 'media/image/2024/04/data-make.png' | relative_url }} "start")  
*选择闻韶楼 or 天山堂/秦岭堂*

### 3. 输入选项

- 第一项：模式选择【参考[运行程序（2）](#2运行程序)】
- 第二项：数据地点（闻韶楼模式下无需输入）
- 第三项：原始查课数据路径（**小表头** + **今天待做数据**）【详见[数据准备（2）](#2到课率原始数据查课助理)】
- 第四项：异常到课数据路径【详见[数据准备（3）](#3异常情况记录备案办公室助理)】
- 第五项：截图文件夹路径【详见[数据准备（4）](#4截图)】
- 第六项：生成文件路径，即文件输出位置

![nor-make-input.png]({{ 'media/image/2023/11/nor-make-input.png' | relative_url }} "input")  
*输入概览*

### 4. 打印输出（用作检查）

**输出**  
![nor-make-report1.png]({{ 'media/image/2023/11/nor-make-report1.png' | relative_url }} "report")

**and another 输出**  
![nor-make-report2.png]({{ 'media/image/2023/11/nor-make-report2.png' | relative_url }} "report")


### 5. 见证奇迹

示例

```text
20231017天山堂                                              # 文件夹
├── 天山堂10月17日学生到课情况统计表.xlsx                     # 到课率表
└── 10月17日榆中校区截图                                     # 文件夹
    ├── 天山堂2023秋季学期异常课堂截图记录（20231017）.xlsx    # 异常情况表
    ├── 20231017天山堂截图1.JPG                              # 截图
    ├── 20231017天山堂截图2.JPG
    └── 20231017天山堂截图3.JPG  
```

| 路径示例 | 表格内容 |
| :---: | :---: |
| ![result1.png]({{ 'media/image/2023/11/result1.png' | relative_url }} "result") **生成总文件夹** | ![result3.png]({{ 'media/image/2023/11/result3.png' | relative_url }} "result") **每日到课率表** |
| ![result2.png]({{ 'media/image/2023/11/result2.png' | relative_url }} "result") **到课率表 + 截图文件夹** | ![result5.png]({{ 'media/image/2023/11/result5.png' | relative_url }} "result") **异常情况表** |
| ![result4.png]({{ 'media/image/2023/11/result4.png' | relative_url }} "result") **异常情况表 + 截图** | |

## 节假日

**Note:** 节假日处理数据的助理需要且只需要处理当天的数据（包括晚上）
{: .notice--info}

**1. 保证输入的到课率数据为对应时间段的数据（eg. 当天1-11节）**

与前面操作相同（略）

**2. 先改变原始数据星期列（查课助理到课率表+办公室助理异常情况表均需更改）为今天真实星期，再将程序输出的到课率表的星期列调回原来的星期**

<p>a. 查课助理到课率表<b>星期列</b>更改</p>

![holiday-checkdata.png]({{ 'media/image/2024/04/holiday-checkdata.png' | relative_url }})

<p>b. 办公室助理异常情况表<b>星期列</b>更改</p>

![holiday-officedata.png]({{ 'media/image/2024/04/holiday-officedata.png' | relative_url }})

补充：Excel单元格快速填充（三步）

<figure class="align-center">
  <img src="{{ 'media/image/2024/04/filldata-choose.png' | relative_url }}" alt="filldata-choose.png">
  <figcaption>第一步</figcaption>
</figure> 

<figure class="align-center">
  <img src="{{ 'media/image/2024/04/filldata-enter.png' | relative_url }}" alt="filldata-enter.png">
  <figcaption>第二步</figcaption>
</figure> 

<figure class="align-center">
  <img src="{{ 'media/image/2024/04/filldata-fill.png' | relative_url }}" alt="filldata-fill.png">
  <figcaption>第三步</figcaption>
</figure> 

<p>c. 程序输出的到课率表<b>星期列</b>调回原值</p>

![output-data.png]({{ 'media/image/2024/04/output-data.png' | relative_url }})

## 程序跑不了

- 输入路径存在**空格**【重命名文件/文件夹，删去空格】
- 原始查课数据未经选择直接丢给程序 【处理方法见[数据准备（2）](#2到课率原始数据查课助理)】
- 原始查课数据中到课人数存在空值 【此时需要赋值为0】

## 程序跑完后

重点是**每日到课率表**

- 加入大表头（**仔细仔细再仔细：日期、节次、地点**）
- 调格式（**字体**，**行高**，**表头加粗**）
- 到课率低于70%标黄
- 调整最后一列备注
- 最后一行加入**备注说明**

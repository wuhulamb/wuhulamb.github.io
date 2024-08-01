---
title:            "高德API使用demo：行政区查询"
author:           "wuhulamb"
date:             "2024-05-19 21:50:00 +0800"
categories:
  - "技术应用"
tags:
  - "高德API"
  - "数据爬取"
  - "Python"
header:
  overlay_image:           "assets/hero-img/posts/world-data.jpg"
---

如今，电子地图已成为每个人生活中不可或缺的一部分，出行导航、购物逛街、聚会吃饭等各种场合都离不开它。不仅如此，它在社会学、经济学、地理学等研究领域也大放光彩，一度成为热点方法。本文以高德API做行政区查询为例，演示如何获取地理数据<!--more-->。（不过可能会有商务打电话要money :upside_down_face:

<figure class="half">
    <img src="{{ 'media/image/2024/05/poi-literature.jpg' | relative_url }}">
    <img src="{{ 'media/image/2024/05/amap-business.jpg' | relative_url }}">
</figure>

## 原理

和[网站]({{ 'blog/2024/04/14/what-is-a-website/' | relative_url }})一样，我们看到的电子地图背后其实是一个巨大的数据库以及一台服务器。当我们搜索某个地方时，相当于向服务器发送了请求，服务器在数据库查询到结果后又将结果返回给我们。所以我们可以使用程序模拟人工搜索，批量发出请求，获取数据。这就是爬虫的基本原理。不过如果使用[高德API](https://lbs.amap.com/)，事情就更加简单了。

API全称Application Programming Interface，作用和函数相近。向接口输入请求数据，再从接口接收返回数据，隐藏不必要的中间过程。使用API获取数据的好处有以下几点：

1. 不会被服务器拦截，放心爬取（不过高德有[每日配额限制](https://lbs.amap.com/api/webservice/guide/tools/flowlevel)
2. 不用分析网页结构，直接接收返回数据

## 代码

### 功能

输入需要查询的省份/城市，画出该行政区以及下一级子行政区的地图。

![polygon.png]({{ 'media/image/2024/05/polygon.png' | relative_url }})

**Input: 安徽省**

**Output:**

![anhui.jpg]({{ 'media/image/2024/05/anhui.jpg' | relative_url }})

注意：

- 查询四个直辖市需要输入xx城区，如北京市输入的是北京城区
- 查询两个特别行政区需要输入xx特别行政区，如香港输入的是香港特别行政区
- 不支持台湾省的详细区划查询
- 输入中国可查询34个省级行政区
- 不支持区县的下一级行政区查询

### 实现

需要安装的库有：

- [requests](https://pypi.org/project/requests/)
- [shapely](https://pypi.org/project/shapely/)
- [geopandas](https://pypi.org/project/geopandas/)
- [matplotlib](https://pypi.org/project/matplotlib/)

使用程序前需要先填入高德API Web类型 key，可在[高德开放平台](https://lbs.amap.com/)注册申请。

```python
# Python 3.8.8
# -*- Coding: UTF-8 -*-
# CreateDate: 2022/3/4 22:39
# Author: wuhulamb
import json
import requests
from shapely.geometry import Polygon
import geopandas as gpd
from matplotlib import pyplot

url = 'https://restapi.amap.com/v3/config/district'
param = {
    'key': '',            # 填入高德API key
    'keywords': '',       # 查询关键字
    'subdistrict': '1',   # 返回数据包括下一级行政区
    'extensions': 'all',  # 控制返回数据详细程度
}

def single_polygon(single_district):
    """get_polygon私有函数, 返回单个Polygon对象"""
    single = []
    for item in single_district.split(';'):
        lon, lat = item.split(',')
        single.append((float(lon), float(lat)))
    return Polygon(single)

def get_polygon(response):
    """返回请求区域中所有的Polygon对象的列表（部分地区包含飞地）"""
    all = json.loads(response.text)
    possible = []       # 存放获取的single_polygon（字符）
    target = []         # 存放处理后的singe_polygon（Polygon对象）
    for _ in all['districts'][0]['polyline'].split('|'):
        possible.append(_)
    for i in possible:
        target.append(single_polygon(i))
    return target

def get_subdistricts(response_text):
    """返回数据格式 {'城关区': ['adcode', (103.825315,36.056948)]}"""
    subdistricts = {}
    js = json.loads(response_text)
    for i in js['districts'][0]['districts']:
        lon, lat = i['center'].split(',')
        subdistricts[i['name']] = [i['adcode'], (float(lon), float(lat))]
    return subdistricts

def main():
    region_name = input('请输入一个你想查询的城市/省份: ')
    param['keywords'] = region_name
    region_all = []
    rep_text = requests.get(url, params=param).text
    districts = get_subdistricts(rep_text)

    for _ in districts:
        param['keywords'] = districts[_][0]
        x = get_polygon(requests.get(url, params=param))
        for item in x:
            region_all.append(item)

    g = gpd.GeoSeries(region_all, crs='epsg:4326')    # 设置坐标系为WGS84，即GPS
    g.plot(facecolor='#87CEFA', edgecolor='#FF6347')  # 设置填充和边界颜色
    pyplot.rcParams['font.sans-serif'] = 'SimHei'     # 设置字体使得中文正常显示
    for i in districts:                               # 标注地名
        pyplot.text(districts[i][1][0], districts[i][1][1], i, ha='center', va='top', fontsize=8)
    pyplot.show()

if __name__ == '__main__':     # 判断程序是否直接运行还是作为包导入
    main()
```

具体实现可参考：

- [高德开发者文档](https://lbs.amap.com/api/webservice/guide/api/district)
- [GeoPandas文档](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.html)

高德API返回的数据是经过加密偏移的，并非真实WGS84坐标系下的数据。不过偏移不大，大概为几百米，同时为了保证代码的简洁性，没有再额外进行坐标转换，想要深入了解可以看看 :point_right: [Coordtransform by wandergis](https://wandergis.com/coordtransform/) & [GitHub Project](https://github.com/wandergis/coordtransform)

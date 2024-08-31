---
title:            "绕过CSDN：关注博主即可阅读全文"
author:           "wuhulamb"
date:             "2024-08-31 19:00:00 +0800"
categories:
  - "仅供娱乐"
tags:
  - "CSDN"
  - "tricks"
header:
  overlay_image:   "assets/hero-img/posts/skyscraper.jpg"
---

## 背景铺垫

[CSDN](https://www.csdn.net/)作为我国规模不小的技术博客写作平台是我梦想开始的地方（也只是我梦想开始的地方 :poop: ，随后就转向[知乎](https://www.zhihu.com/)，接着又转向更加专注更少广告且更少推广的个人博客）。其中最主要的原因是<!--more-->：

- 广告太多
- 玩的太花（**关注博主即可阅读全文**，最不能忍的就是这个）
- 内容质量高低不一（而且低的偏多 :poop: ）
- 忘了一条：未登录不能复制 ... （强调这一点是因为登录意味着账号，而这是阻挡知识分享的一面高墙，尤其对比[GitHub](https://github.com/)在不用登录的情况下就可以clone仓库）

可是，你会发现每次搜索（这里指用中文）的前五条结果必然会有CSDN，这一方面是CSDN里确实有很多相关的技术文章，另一方面是CSDN通过一些手段，使中文检索充斥着它的内容（点名[某度](https://www.baidu.com/)）。当然许多网站都会做SEO优化，可是CSDN实在做得有点过了。加上前段时间发生了[CSDN旗下GitCode被曝批量搬运GitHub项目](https://www.ithome.com/0/778/049.htm)的事，让我对CSDN的好感直线下降。

但是，有的时候你会遇到不得不看CSDN的情况。就比如说，最近我在查阅GBDT算法的资料，然后在GitHub上找到了一个介绍这个算法的[仓库](https://github.com/Freemanzxp/GBDT_Simple_Tutorial)（700多stars！），这时发现介绍算法的文章是在CSDN上 :poop:

<figure class="align-center">
  <img src="{{ 'media/image/2024/08/GBDT-github.jpg' | relative_url }}" alt="GBDT-github.jpg">
  <figcaption>放在CSDN上的Blog</figcaption>
</figure>

然后当我无可奈何地点开链接兴致勃勃地往下阅读时，突然发现**关注博主即可阅读全文** :poop:

<figure class="align-center">
  <img src="{{ 'media/image/2024/08/not-well.jpg' | relative_url }}" alt="not-well.jpg">
  <figcaption>CSDN：关注博主即可阅读全文</figcaption>
</figure>


## 如何绕过

### 1. 打开浏览器开发者模式

**方法一：**

<figure class="align-center">
  <img src="{{ 'media/image/2024/08/browser-devlop1.jpg' | relative_url }}" alt="browser-devlop1.jpg">
</figure>

**方法二：**

<figure class="align-center">
  <img src="{{ 'media/image/2024/08/browser-devlop2.jpg' | relative_url }}" alt="browser-devlop2.jpg">
</figure>

**方法三：**

按F12键打开（大多数情况ok，少数电脑默认快捷键不是这个）

### 2. 删除 `关注博主即可阅读全文` div元素

蓝色标注是红色标注第二步找到 `<div class="hide-article-box hide-article-pos text-center">` 元素的步骤

<figure class="align-center">
  <img src="{{ 'media/image/2024/08/del-div.jpg' | relative_url }}" alt="del-div.jpg">
</figure>

### 3. 删除 `height: 2000px;` 属性

同上，先找到 `<div id="article_content" class="article_content clearfix" style="height: 2000px; overflow: hidden;">` 元素，再删除 `height: 2000px;` 属性即可无障碍阅读了！

<figure class="align-center">
  <img src="{{ 'media/image/2024/08/del-height2000.jpg' | relative_url }}" alt="del-height2000.jpg">
  <figcaption>（双击鼠标左键也可以编辑）</figcaption>
</figure>

## 为什么不直接使用Edge的阅读器模式

本着能少做一步绝不多做一步的懒人想法（Unix哲学也有一条著名的KISS原则：keep it simple, stupid），既然可以使用Edge的阅读器模式通览全篇，为什么还要那么麻烦用浏览器开发者模式删除前端代码？

<figure class="align-center">
  <img src="{{ 'media/image/2024/08/edge-read.jpg' | relative_url }}" alt="edge-read.jpg">
  <figcaption>Edge阅读器模式下不忍直视的数学公式</figcaption>
</figure>

不是咱看不懂 [`MathJax`](https://www.mathjax.org/) ，而是实在没必要。那么多的数学符号已经够让人头大了，何苦再折磨自己以代码的形式去阅读 :upside_down_face:

最后附上相关链接，感兴趣的朋友可以试试 :point_down:

<p style="word-break: break-word;"><a href="https://blog.csdn.net/zpalyq110/article/details/79527653">https://blog.csdn.net/zpalyq110/article/details/79527653</a></p>

---
title:            "网站的背后是 . . ."
author:           "wuhulamb"
date:             "2024-04-14 21:30:00 +0800"
last_modified_at: "2024-05-12 15:00:00 +0800"
categories:
  - "理论学习"
tags:
  - "website"
  - "GitHub Pages"
header:
  overlay_image:           "assets/hero-img/posts/mountain.jpg"
---

几乎所有人都使用过浏览器，但你真的知道浏览器是如何工作的吗？为什么可以使用浏览器听音乐、看视频甚至玩游戏、购物？另一边，网站又是如何向我们提供这些服务的？本文将揭露网站背后的真相，还将还原一个最简单的网站<!--more--> :pinching_hand: 。

## User

作为用户，你分得清浏览器和搜索引擎吗？

### 浏览器

我们每天都在上网，而提到上网就离不开浏览器。可能许多人会说，自己几乎不用浏览器，也很少看网站。那是因为许多软件都内置了自己的浏览器，只要你点开了一个链接，便是在使用浏览器访问网站。这个链接对应的网址叫做**统一资源定位符**（Universal Resource Locator），简称**URL**，用来确定要访问的是哪个网站。

<figure class="align-center">
  <img src="{{ 'media/image/2024/04/browser-and-website.jpg' | relative_url }}" alt="browser-and-website.jpg">
  <figcaption>浏览器和网站的默契</figcaption>
</figure> 

当我们在浏览器的网址栏输入一个URL，并按下回车键时，其实就是在向网站发送请求。网站收到请求后，会将数据发送给浏览器，浏览器接收后再进行解析渲染，最后将五彩缤纷的内容呈现在我们面前。

### 搜索引擎

直接输入URL访问网站虽然很酷，但是更多的时候我们会使用搜索引擎找到我们需要的东西。比如，[谷歌](https://www.google.com)、[必应](https://www.bing.com/)，还有[某度](https://www.baidu.com/)。这些搜索引擎也是网站，是比较特殊的网站，通过它们我们可以轻松找到我们需要的网页。

## Developer

作为开发者，如何搭建一个网站？

### 服务器

许多文章或是新闻中都会说到服务器，那服务器到底是什么呢？

<figure class="half">
    <img src="{{ 'media/image/2024/04/sever-cluster.jpg' | relative_url }}">
    <img src="{{ 'media/image/2024/04/sever-micro.jpg' | relative_url }}">
    <figcaption>集群服务器与微型服务器</figcaption>
</figure>

可能许多人印象中的服务器是一个庞然大物，但是它也可以只是一块集成了CPU、GPU、内存、显卡的一块计算卡，说到底一台服务器只是一台性能不错的计算机。唯一的区别在于服务器作为服务的提供者，需要时时刻刻响应众多客户端的请求，并作出反应，而一台普通的计算机可以断网，可以关机，可以 ... :sunglasses:

网站服务器同样如此，在接收到浏览器的请求时，它需要作出响应，将请求的数据发给浏览器。

### 网页

一个网页只有一个HTML文件，它会调用CSS、JavaScript或者其他media文件（如音视频文件），经过渲染最后呈现在我们面前。

- **HTML（骨架）**

  决定网页的元素、内容、布局等

- **CSS（修饰）**

  对网页元素的颜色、形状等属性进行定义

- **JavaScript（操作）**

  与页面的交互，如动画展示、点击反馈等（许多广告以及登录即可复制都是通过js实现的）

- **media（文件）**
  
  嵌入媒体文件，如图像、音频、视频等

**代码示例**

点击 :point_right: [https://wuhulamb.github.io/a-simple-webpage/](https://wuhulamb.github.io/a-simple-webpage/) 查看示例（部分代码参考自互联网，详见[引用](#引用)）

*目录结构*

```text
.
├── index.html
└── assets
    ├── css
    │   └── main.css
    └── js
        └── main.js
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
    <head>
        <title>原来你在这儿！</title>
        <link rel="stylesheet" href="assets/css/main.css">   <!-- 嵌入main.css -->
        <script src="assets/js/main.js" defer></script>      <!-- 嵌入main.js -->
    </head>
    <body>
        <h1>Halo</h1>                  <!-- 1级标题 -->
        <p id="demo">你在哪儿？</p>     <!-- 段落 -->
        <button type="button" onclick="myFunction()">Click me</button>  <!-- 按钮 -->
    </body>
</html>
```

```css
/* assets/css/main.css */
body {
  background-color: lightblue;  /* 背景颜色 */
}

h1 {
  color: navy;                  /* 标题颜色 */
}
```

```js
// assets/js/main.js
function myFunction() {   // 替换段落
  document.getElementById("demo").innerHTML = "我在这儿！";
}
```

**实践验证**

<p>1. 打开浏览器开发者选项</p>

![developer-tool.png]({{ 'media/image/2024/04/developer-tool.png' | relative_url }})

<p>2. 通过浏览器开发者选项查看接收到的文件（如果是空白，请刷新网页）</p>

![a-simple-webpage.png]({{ 'media/image/2024/04/a-simple-webpage.png' | relative_url }})

**在github上搭建网站** 请看这篇博客 :point_right: [玩转 github pages]({{ 'blog/2024/02/29/github-pages/' | relative_url }})

### 网站

网站是互相链接的网页集合，这些网页共享一个域名（例如本站的各个页面都有wuhulamb.github.io作为前缀）。每个网页又是由一个HTML，以及CSS、JavaScript、media等文件共同组织形成的。所以，可以认为，一个网站就是服务器上的一个文件夹，里面有各种HTML、CSS、JavaScript或者media文件，这些文件相互关联，由各个HTML文件组织调用，最终经过浏览器的解析渲染呈现在了我们眼前。

至于浏览器如何向网站发出请求，以及服务器如何作出回应发送数据，涉及到计算机网络基本原理相关内容，与本篇博客关系不大，故不再展开。（有时间的话可能会再写一篇相关的博客 :poop:

## 引用

1. [What is the difference between webpage, website, web server, and search engine?（英文）](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/Pages_sites_servers_and_search_engines)
2. [JavaScript Example（英文）](https://www.w3schools.com/js/js_whereto.asp)
3. [CSS Example（英文）](https://www.w3schools.com/css/css_howto.asp)

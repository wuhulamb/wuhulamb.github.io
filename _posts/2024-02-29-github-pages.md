---
title:            "玩转github pages"
author:           wuhulamb
date:             "2024-02-29 16:40:00 +0800"
categories:
  - "计算机"
tags:
  - "github pages"
---

## 它能做什么

将仓库变成网站！！

## 为什么可以

它默认使用[jekyll](https://jekyllrb.com/)[^1]作为static site generator来将仓库中的HTML, CSS, and JavaScript等静态文件转化成_site文件夹（我们不可见）下的站点文件（其实就是html）。我们访问<!--more-->网址时，它将对应的文件发给浏览器，然后浏览器进行渲染就成了最后看到的网页。

除了使用默认的jekyll，我们还可以通过自定义GitHub Actions workflow来创建一个build process（有待进一步探索:eyes:

这里有更详细的介绍:point_right:[官方文档](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)

## 开始搭建自己的网站！

### 第一步：创建一个github账号
网址：[https://github.com/](https://github.com/)

### 第二步：创建一个xxx.github.io仓库

这里的xxx为你的username，例如我的是wuhulamb

![github-create-a-repository.png](/media/image/2024/02/github-create-a-repository.png)

后面的选项默认即可

### 第三步：设置仓库

![github-pages-setting.png](/media/image/2024/02/github-pages-setting.png)  
这里以普通仓库为例进行设置，xxx.github.io同理

### 第四步：加入一个index.html文件

![github-add-file.png](/media/image/2024/02/github-add-file.png)  
比较原始的添加文件的方法，使用git会更加方便

html示例

```html
<!DOCTYPE html>
<html>
    <head>
        <title>我在这儿！</title>
    </head>
    <body>
        <h1>Halo</h1>
        <p>原来你在这儿！</p>
    </body>
</html>
```

### 第五步：访问你的网站！

https://xxx.github.io/

示例：[https://wuhulamb.github.io/test/](https://wuhulamb.github.io/test/)

---

[^1]: jekyll是一个转换工具，可以将plain text转换成blog site。github的仓库自带此功能，只需按照要求放入相关文件即可。

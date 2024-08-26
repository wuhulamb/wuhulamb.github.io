---
title:            "giscus 评论测试"
author:           "wuhulamb"
date:             "2024-07-31 10:00:00 +0800"
categories:
  - "其他"
tags:
  - "博客评论"
  - "giscus"
toc: false
header:
  overlay_image:   "assets/hero-img/posts/building.jpg"
---

一直想在博客里加入评论功能，今天终于实现啦！

本博客使用[giscus](https://giscus.app/)评论系统，登录[GitHub](https://github.com/)即可评论。

登录时会出现 `GitHub OAuth flow` ，点击 `Authorize giscus` 确认授权<!--more-->。关于授权，更多信息可见：[https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps](https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps)

<figure class="align-center">
  <img src="{{ 'media/image/2024/07/giscus-OAuth.png' | relative_url }}" alt="giscus-OAuth.png">
  <figcaption>giscus 授权页面</figcaption>
</figure>

取消授权可通过 `Settings` >> `Applications` >> `Authorized GitHub Apps` >> `Revoke`

<figure class="align-center">
  <img src="{{ 'media/image/2024/07/revoke-giscus.png' | relative_url }}" alt="revoke-giscus.png">
  <figcaption>取消授权</figcaption>
</figure>

如果不想授权，也可以到仓库对应讨论位置直接评论（本篇博客[点此跳转](https://github.com/wuhulamb/wuhulamb.github.io/discussions/1)）

评论后，如果有人回复，会发送邮件进行通知（Github通过邮箱注册，邮件地址就是注册时填入的邮箱）

支持多种表达形式：

- [Markdown语法](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [emoji](https://github.com/ikatyang/emoji-cheat-sheet)
- [Reactions](https://docs.github.com/en/rest/reactions/reactions)
- Picture & GIF
- 几乎所有Github支持的表达（将帖子顶上去的功能似乎还不支持） ...

总的来说，体验是非常非常棒的。

## 欢迎测试 👇👇👇

---
title:            "初识递归：什么是递归"
author:           "wuhulamb"
date:             "2024-01-31 17:30:00 +0800"
last_modified_at: "2024-09-12 15:50:00 +0800"
categories:
  - "理论学习"
tags:
  - "recursion"
  - "Python"
header:
  overlay_image:   "assets/hero-img/posts/stairs.jpg"
---

递归在数学中是一个常见的概念，著名的斐波那契数列就是通过递归来定义的（后一项等于前两项之和），但是在计算机中又是怎么实现递归的呢？本文就通过几个简单的例子来说明。（编程语言： `Python 3.8.8` ）<!--more-->

## 引子：计算阶乘

先看一个简单的例子：求 n!

![factorial-recursion.jpg]({{ 'media/image/2024/01/factorial-recursion.jpg' | relative_url }})  
:arrow_up: 通过递归计算 5! 

```python
# Python3.8.8
def factorial(n: int) -> int:
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1
print([factorial(_) for _ in range(1, 6)])  # 遍历1,2,3,4,5，代入factorial函数中

# result
# [1, 2, 6, 24, 120]
```

不难发现，递归算法最显著的特征就是**在函数的内部调用了函数本身**。这意味着调用函数后，不能立刻得到结果，需要等待内部函数返回结果，再进行下一步的运算。所以使用递归需要**提前考虑好函数的返回结果是什么**，这样在编写函数时才不会觉得无从下手。由此也引出了一个问题，递归调用何时停止？一个可以正常运行的递归函数必须要设置一个**停止递归的条件**。在上面的例子中，即 `n <= 1` 。（这里停止递归就是指没有调用函数本身就可以返回结果）

## 深入：输出排列结果

### 题目

再来看一个更有挑战的例子：输入一个列表（如 `['a', 'b', 'c', 'd']` ）和一个正整数 **n** ，返回 **n** 个列表元素的排列。

    Input: (['a', 'b', 'c', 'd'], 2)
    Output: [['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'a'], ['b', 'c'], ['b', 'd'], ['c', 'a'], ['c', 'b'], ['c', 'd'], ['d', 'a'], ['d', 'b'], ['d', 'c']]

### 代码

```python
# Python3.8.8
def permutation(data: list, n: int) -> list:
    result = []
    for k, i in enumerate(data):               # k是index，i是value
        if n > 1:
            new = data.copy()                  # 拷贝原始输入列表至new
            new.pop(k)                         # 将new中下标为k的元素踢出，即i（排列的第一个元素）
            # 后面的for循环就是将元素i和permutation(new, n - 1)中的每一个结果拼接起来，然后放入result里面
            for j in permutation(new, n - 1):  # permutation(new, n - 1) -> 在没有元素i的列表里选择剩下n - 1个元素排列
                temp = [i]                     # 这里也能看出i是排列的第一个元素
                for m in j:                    # j是permutation(new, n - 1)返回的一个排列
                    temp.append(m)
                result.append(temp)            # temp就是一个完整的排列了
        else:                                  # n = 1，即从列表元素中挑一个元素排的情况
            result.append([i])                 # !WARNING 此处是[i]，不是i，因为result里的每一个元素都是一种排列的方案 ，即temp列表
    return result
```

### 思路

递归的本质是**降维**。这里的降维是指将复杂的问题变简单，然后重复下去，直到问题简单到可以直接得到解决（即不需要再调用递归函数就能解决）。

以 `data=['a', 'b', 'c', 'd', 'e'], n=3` 为例，可以认为是先从列表中挑了 **1** 个元素放在第一个，然后再从剩下的元素中挑选了 **2** 个放在后面。此时问题得到了简化，由 `n=3` 变成了 `n=2` ，而解决 `n=2` 的过程类似，直到问题简化为 `n=1` 的情况。此时列表中的每个元素就是一种排列，问题简化到了可以直接解决的程度，再一层一层将得到的结果返回上去就可以得到最终的结果，这就是程序的实现思路。

## 实战

### 练习1：输出组合结果

输入一个列表（如 `['a', 'b', 'c', 'd']` ）和一个正整数 **n** ，返回 **n** 个列表元素的组合。

    Input: (['a', 'b', 'c', 'd'], 2)
    Output: [['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['b', 'd'], ['c', 'd']]

### 练习2：汉诺塔问题

汉诺塔问题：有三根柱子A、B、C，A柱子从上往下依次是1,2,3,..,n号圆盘，其中序号越大表示圆盘越大。如何将圆盘从A柱子挪到C柱子上？

要求：
- 一次挪动一个圆盘
- 只能挪动每根柱子最上面的圆盘
- **小圆盘必须在大圆盘上面**

![Tower-of-Hanoi.jpg]({{ 'media/image/2024/01/Tower-of-Hanoi.jpg' | relative_url }} "Tower-of-Hanoi")

如果体会不深，可以玩一下:point_right: [汉诺塔游戏](https://www.saolei.games/h.html)

## 答案

### 练习1：输出组合结果

和排列问题很像，唯一的区别是，在遍历完某元素的情况后，排列不会去除该元素，而组合会去除它，即下面代码中的 `new.pop(0)`

```python
# Python 3.8.8
def combination(data: list, n: int) -> list:
    result = []
    new = data.copy()                          # 在for循环外面拷贝，意味着下面的new.pop(0)会永久地踢出某元素
    for i in data:
        if n > 1:
            new.pop(0)                         # 永久地踢出new中的第一个元素，即i（后面再调用combination(new, n - 1)时不会再有元素i）
            for j in combination(new, n - 1):  # combination(new, n - 1) -> 在没有元素i的列表里选择剩下n - 1个元素组合
                temp = [i]
                for m in j:
                    temp.append(m)
                result.append(temp)
        else:
            result.append([i])
    return result
```

### 练习2：汉诺塔问题

汉诺塔问题递归解决的基本思想是先将Start(Source)处的n - 1个盘子挪到Middle(Auxiliary)，再将n号盘子挪到Goal(Destination)，最后再将n - 1个盘子从Middle(Auxiliary)挪到Goal(Destination)。

![Tower-of-Hanoi-recursion.png]({{ 'media/image/2024/01/Tower-of-Hanoi-recursion.png' | relative_url }})

```python
# Python 3.8.8
def hannoi(n: int, start: str, middle: str, goal: str) -> list:      # n为start柱子上的圆盘个数，start为初始柱子名称，middle为中间柱子名称，goal为目标柱子名称
    result = []
    if n > 1:
        for i in hannoi(n - 1, start, goal, middle):  # 此处hannoi函数返回n - 1个圆盘从start挪到middle的步骤
            result.append(i)
        result.append([n, start, goal])               # 将n号盘子从start挪到goal
        for i in hannoi(n - 1, middle, start, goal):  # 将n - 1个盘子从middle挪到goal
            result.append(i)
    else:                                             # n = 1时直接将1号盘子从start挪到goal
        result.append([1, start, goal])
    return result
```

## 思考：非递归方法实现递归？

在计算机中，递归问题是否可以用非递归的方法解决？如何实现？

## 致谢

感谢 pzm 仔细阅读本篇文章，并指出了代码中的一处关键问题！

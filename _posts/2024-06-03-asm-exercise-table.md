---
title:            "「习题」- 使用汇编处理表格"
author:           "wuhulamb"
date:             "2024-06-03 22:30:00 +0800"
last_modified_at: "2024-07-08 15:35:00 +0800"
categories:
  - "理论学习"
tags:
  - "8086"
  - "ASM"
header:
  overlay_image:           "assets/hero-img/posts/architecture.jpg"
---

习题出自《汇编语言（第4版）》王爽著 清华大学出版社出版 第八章 实验7：寻址方式在结构化数据访问中的应用。使用8086CPU指令。

## 题目

Power idea 公司从1975年成立一直到1995年的基本情况如下<!--more-->。

| 年份 | 收入（千美元） | 雇员（人） | 人均收入（千美元） |
| :---: | :---: | :---: | :---: |
| 1975 | 16 | 3 | ? |
| 1976 | 22 | 7 | ? |
| 1977 | 382 | 9 | ? |
| 1978 | 1356 | 13 | ? |
| 1979 | 2390 | 28 | ? |
| 1980 | 8000 | 38 | ? |
| ... | ... | ... | ... |
| 1995 | 5937000 | 17800 | ? |

下面的程序中，已经定义好了这些数据：

```text
assume cs:codesg

data segment
  db '1975','1976','1977','1978','1979','1980','1981','1982','1983'
  db '1984','1985','1986','1987','1988','1989','1990','1991','1992'
  db '1993','1994','1995'
  ;以上是表示21年的21个字符串

  dd 16,22,382,1356,2390,8000,16000,24486,50065,97479,140417,197514
  dd 345980,590827,803530,1183000,1843000,2759000,3753000,4649000,5937000
  ;以上是表示21年公司总收入的21个dword型数据

  dw 3,7,9,13,28,38,130,220,476,778,1001,1442,2258,2793,4037,5635,8226
  dw 11542,14430,15257,17800
  ;以上是表示21年公司雇员人数的21个word型数据
data ends

table segment
  db 21 dup ('year summ ne ?? ')
table ends
```

编程，将data段中的数据按如下格式写入到table段中，并计算21年中的人均收入（取整），结果也按照下面的格式保存在table段中。

![asm-exercise-style.jpg]({{ 'media/image/2024/06/asm-exercise-style.jpg' | relative_url }})

## 分析

> 一个好用但常常被忽视的寄存器——ES寄存器 ......

<p><b>1. 要求</b></p>

将data里的数据进行整除运算，并按照格式要求存入table中

<p><b>2. 思路</b></p>

用ds表示data，es表示table，栈临时存储cx和bx，将data中的数据填入table中

## 代码

```text
assume cs:codesg,ds:data,ss:stack,es:table

data segment
  db '1975','1976','1977','1978','1979','1980','1981','1982','1983'
  db '1984','1985','1986','1987','1988','1989','1990','1991','1992'
  db '1993','1994','1995'
  ;以上是表示21年的21个字符串

  dd 16,22,382,1356,2390,8000,16000,24486,50065,97479,140417,197514
  dd 345980,590827,803530,1183000,1843000,2759000,3753000,4649000,5937000
  ;以上是表示21年公司总收入的21个dword型数据

  dw 3,7,9,13,28,38,130,220,476,778,1001,1442,2258,2793,4037,5635,8226
  dw 11542,14430,15257,17800
  ;以上是表示21年公司雇员人数的21个word型数据
data ends

table segment
  db 21 dup ('year summ ne ?? ')
table ends

stack segment         ; 临时保存cx和bx
 dw 2 dup (0)
stack ends

codesg segment
start: mov ax,stack   ; stack初始化
       mov ss,ax
       mov sp,4
       mov ax,data    ; data初始化
       mov ds,ax
       mov ax,table   ; table初始化
       mov es,ax

       mov bp,0       ; table索引
       mov bx,0       ; data索引
       mov cx,21      ; 大循环计数

    s: push cx        ; cx入栈

       push bx        ; year数据填入栈中
       mov si,0
       mov cx,4
       add bx,bx      ; bx乘2，适配year索引
   s0: mov al,[bx + si]
       mov es:[bp + si],al
       inc si
       loop s0
       pop bx

       mov si,bx                     ; 计算总收入/人数的商
       mov ax,[bx + si + 84]         ; 被除数低位 等效于[bx + bx + 84]
       mov dx,[bx + si + 84 + 2]     ; 被除数高位 等效于[bx + bx + 84 + 2]
       div word ptr [bx + 168]

       mov es:[bp + 13],ax           ; 先填入ax，即总收入/人数的商
       mov byte ptr es:[bp + 4],20h  ; 其余数据出栈填入table，20h为空格
       mov ax,[bx + si + 84]
       mov es:[bp + 5],ax
       mov ax,[bx + si + 84 + 2]
       mov es:[bp + 7],ax
       mov byte ptr es:[bp + 9],20h
       mov ax,[bx + 168]
       mov es:[bp + 10],ax
       mov byte ptr es:[bp + 12],20h
       mov byte ptr es:[bp + 15],20h

       pop cx            ; cx出栈还原
       add bx,2          ; data索引加2 byte实现取下一个数据
       add bp,16         ; table索引加16 byte实现换行
       loop s

       mov ax,4c00h      ; 程序中断然后结束
       int 21h
codesg ends
end start
```

## 调试

<p><b>1. 代码编译连接正常</b></p>

![asm-exercise-image5.png]({{ 'media/image/2024/06/asm-exercise-image5.png' | relative_url }})

<p><b>2. 初始化数据正常</b></p>

栈初始化正常

![asm-exercise-image6.png]({{ 'media/image/2024/06/asm-exercise-image6.png' | relative_url }})

data初始化正常

![asm-exercise-image7.png]({{ 'media/image/2024/06/asm-exercise-image7.png' | relative_url }})

table初始化正常

![asm-exercise-image8.png]({{ 'media/image/2024/06/asm-exercise-image8.png' | relative_url }})

<p><b>3. 程序正常运行</b></p>

查看最终table里的数据

![asm-exercise-image9.png]({{ 'media/image/2024/06/asm-exercise-image9.png' | relative_url }})

## 补充

<p><b>1. div指令</b></p>

| 除数 | 被除数 | 商 | 余数 |
| :---: | :---: | :---: | :---: |
| 8位 | AX | AL | AH |
| 16位 | AX（低位）、DX（高位） | AX | DX |

```text
div reg
div 内存单元                 ; 需要加上 byte ptr / word ptr

div byte ptr ds:[0]
div word ptr es:[0]
div byte ptr [bx + si + 8]  ; ds:[bx + si + 8]
div word ptr [bx + si + 8]  ; ds:[bx + si + 8]
```

<p><b>2. mul指令</b></p>

| 乘数 | 被乘数 | 积 |
| :---: | :---: | :---: |
| 8位 | AL | AX |
| 16位 | AX | AX（低位）、DX（高位） |

```text
mul reg
mul 内存单元                 ; 需要加上 byte ptr / word ptr

mul byte ptr ds:[0]
mul word ptr es:[0]
mul byte ptr [bx + si + 8]  ; ds:[bx + si + 8]
mul word ptr [bx + si + 8]  ; ds:[bx + si + 8]
```

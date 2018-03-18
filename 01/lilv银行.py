#!/usr/bin/env python
#-*- coding:utf-8 -*-

money=1000

xili=1000*0.003
sum=0
# 计算十年后本金+利息
for i in range(1,11):
    sum+=xili
    print(sum)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#arr = [45,67,122,65,89,44,66,12,5,90,4,13,19,2,6,84,47]
stats = [('a',10),('b',5),('c',1),('d',20)]

arr_lenth = len(stats)
while arr_lenth:
    for i in range(arr_lenth-1):
        if stats[i][1] > stats[i+1][1]:
            stats[i],stats[i+1] = stats[i+1],stats[i]
        print(stats)
    arr_lenth-=1        
print(stats)

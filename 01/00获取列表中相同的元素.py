#!/usr/bin/env python3
#encoding:utf-8

nums_1=[1,2,3,4,5,3,10,11]
nums_2=[1,2,3,1,4,5,5,3,12,34]

nums_3=[]

for i in nums_1:
    if (i in nums_2) and (i not in nums_3):
        nums_3.append(i)
print(nums_3)

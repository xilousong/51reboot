#!/usr/bin/env python3
#encoding:utf-8

num = [6,11,7,9,4,2,1]
#count=len(num)

#while count:
for x in range(len(num)):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            num[i],num[i+1] = num[i+1],num[i]
        print(num)
  #  count -= 1

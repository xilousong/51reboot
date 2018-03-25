#!/usr/bin/env python3
#encoding:utf-8

nums = [5, 8, 7, 10, 20, 2, 6, 9]

Sum = 0
count = 0

for i in nums:
    Sum += i
    count += 1 
print('sum=%s,avrage=%s' % (Sum,Sum/count))

#!/usr/bin/env python3
# encoding: utf-8

nums = [5, 8, 7, 10, 20, 2, 6, 9]
maxnum = 0
#maxindx = 0
#index = 0
#for i in nums:
#    if i > maxnum:
#        maxnum = i
#print(nums.index(maxnum),maxnum)

for index  in range(len(nums)):
    if nums[index] > maxnum:
        maxnum = nums[index]
        maxindx = index
 #   index += 1
print(maxindx,maxnum)

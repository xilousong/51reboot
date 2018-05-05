#!/usr/bin/env python

path = 'access.txt'

flog = open('./access.txt','rt')

d={}

for i in range(10):
    for line in flog.readlines():
        l_list = line.split()    
        if (l_list[0],l_list[6],l_list[8]) not in d:
            d[(l_list[0],l_list[6],l_list[8])] = 1
        else:
            d[(l_list[0],l_list[6],l_list[8])] += 1

d_list =list(d.items())
for i in range(len(d_list)-1):
    if d_list[i][1] > d_list[i+1][1]:
        d_list[i],d_list[i+1] = d_list[i+1],d_list[i]
        for i in d_list[-1:-11:-1]:
            print(i)

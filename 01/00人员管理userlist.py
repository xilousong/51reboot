#!/usr/bin/env python3
#encoding: utf-8

users = []

users.append((1, 'kk', 29, '185xxxxxx'))
users.append((2, 'wd', 28, '186xxxxxx'))
users.append((3, 'woniu', 30, '187xxxxxx'))


#print('|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'.format('ID','姓名','年龄','联系方式'))
print('|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'.format('ID','NAME','AGE','PHONE'))
print('-'*50)
for i in range(len(users)):
    print('|{0:^10d}|{1:^10s}|{2:^5d}|{3:^15s}|'.format(users[i][0],users[i][1],users[i][2],users[i][3]))

#!/usr/bin/env python
# encoding: utf-8



def maopao():
    #content=input('请输入随机输入数字，以‘，’分开:')
    #content_new=list(content.split(','))
    content_new=[3,1,6,12,8,2,23,67,21,11,16,33,25,78,40,123,121,61,55,38,80,300]

    for i in range(len(content_new)-1):
        for i in range(len(content_new)-1):
            if int(content_new[i]) > int(content_new[i+1]):
                content_new[i],content_new[i+1] = content_new[i+1],content_new[i]
    print(content_new)


if __name__ == '__main__':
    maopao()

#!/usr/bin/env python3
#encoding:utf-8

task=[]

while True:
    input_txt = input("请输入(do或者其他)：")

    if input_txt == 'do':
        if len(task) == 0:
            print('今天任务做完了。。。')
            break
        else:
            print('任务是：%s' %(task.pop(0)))
    else:
        task.append(input_txt)


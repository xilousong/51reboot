#!/usr/bin/env python
# encoding: utf-8

users={
   1:{'name':'song','age':30,'tel':1311,'pwd':'12345'},
   2:{'name':'dl','age':28,'tel':1312,'pwd':'12345'},
   3:{'name':'xy','age':4,'tel':1313,'pwd':'12345'},
   4:{'name':'qy','age':2,'tel':1314,'pwd':'12345'}


}


login=False

for i in range(3):
    txt=input('请输入验证信息(用户名/密码): ')
    username,password = txt.split('/')
    for k,user in users.items():
        if user['name'] == username and user['pwd'] == password:
            login=True  
            break
    if login:
        print('登录成功。')
        break
    else:
        print('用户名或密码输入错误，请重新输入。')
else:
    print("连续3次验证失败，已退出。")

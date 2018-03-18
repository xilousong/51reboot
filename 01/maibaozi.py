#encoding:utf-8

print("程序员")
Juge = input("你看到西瓜了吗(Y/N): ")
money = 100

print("买一斤包子")
#money=100 - 10

if Juge == 'Y':
    print("买一斤包子10元")
    money-=10
print('剩余金额：' + str(money))

print("程序员的老婆")
Juge = input("你看到西瓜了吗(Y/N): ")
money = 100

print("买一斤包子")
money=100 - 10

if Juge == 'Y':
    print("买一个西瓜话费20元")
    money-=20
    print('剩余金额：' + str(money))
else:
    print('剩余金额：' + str(money))

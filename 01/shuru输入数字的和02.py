#encoding:utf-8

Sum=0
n=0

while True:
    input_txt = input("请输入：")
    if input_txt == 'exit':
        break
    n += 1
    Sum += float(input_txt)

if n != 0:
    print(Sum,Sum/n)
else:
    print(0,0)
    

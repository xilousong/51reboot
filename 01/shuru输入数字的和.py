##encoding: utf-8
#input_txt = input("请输入一个数字或者(exit): ")
#n = 0
#avage = 0
#sum = 0
#
#while input_txt != 'exit':
#    sum += float(input_txt)
#    n+=1
#    input_txt = input("请输入一个数字或者(exit): ")
#    
#
#if n == 0:
#    print('一共输入了%s次，总和为%s，平均值为%s' % (n,sum,0))
#if n != 0:
#    print('一共输入了%s次，总和为%s，平均值为%s' % (n,sum,sum/n))

input_txt = input("请输入一个数字或者exit: ")

n = 0
sum = 0

while input_txt != 'exit':
    n += 1
    sum += float(input_txt)
    input_txt = input("请输入一个数字或者exit: ")

if n != 0:
    print("sum：%s , avarage: %s" % (sum,sum/n))
else:
    print("sum：%s , avarage: 0" % (sum))


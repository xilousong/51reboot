#encoding:utf-8

year = int(input("请输入一个年份(如:1900): "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('%s 年是闰年' %(year))
else:
    print('%s 年不是闰年' %(year))
    

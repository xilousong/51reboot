#encoding:utf-8

score = float(input('请输入你的分数：'))

if score >= 90:
    print('A')
if score >=80 and score < 90:
    print('B')
if score >=70 and score < 80:
    print('C')
if score >=60 and score < 70:
    print('D')
if score < 60:
    print('E')

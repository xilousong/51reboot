INPUT=input('please input: ')
if  INPUT == "list":
    print("|{0:^10s}|{1:^5s}|{2:^15s}|".format("姓名","年龄","联系方式"))
    print('-'*42)
    for i in list(users.items()):
        print("|{0:^10s}|{1:^5d}|{2:^15s}|".format(i[0],i[1]['age'],i[1]['tel']))

#!/usr/bin/env python3
# encoding: utf-8

f = open('/root/51reboot/01/a.txt','rt')
#while True:
#    txt = f.readline()
#    if txt != '':
#        print(txt)
#    else:
#        break

for line in f:
    print(line)

f.close()

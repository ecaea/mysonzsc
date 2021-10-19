# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a,b,c,d=0,0,0,0
flag1,flag2=0,0
num=int(input())
if num %2==0:
    flag1=1
if num>4 and num <=12:
    flag2=1
if flag1==1 and flag2==1:
    a=1
if flag1==1 or flag2==1:
    b=1
#this code belongs to 21161513wangyiming
if (flag1==1 and flag2==0) or (flag2==1 and flag1==0):
    c=1
if flag1==0 and flag2==0:
    d=1
print(a,b,c,d)
    
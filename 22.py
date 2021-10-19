# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:56:17 2021

@author: Administrator
"""

m=int(input())

for i in range(0,m):
    c=i%10
    b=int((i%100-c)/10)
    a=i//100
    if (a**3+b**3+c**3)==i and i!=0 and i!=1:
        print(i)
#this code belongs to 21161513wangyiming        
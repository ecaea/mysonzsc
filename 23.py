# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:08:42 2021

@author: Administrator
"""

def counter(x,m):
    s=0
    while x>0:
        if x%10==m:
            s+=1
        x=(x-x%10)/10
    return s
        
        
m,n=map(int,input().split())
sum=0
for i in range(1,n+1):
    sum+=counter(i,m)
print(sum)
#this code belongs to 21161513wangyiming
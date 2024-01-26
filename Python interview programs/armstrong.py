# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:18:14 2022

@author: amar
"""

a=int(input("enter the number"))
temp=a
n=0
while(temp>0):
    b=temp%10
    n=n+(b*b*b)
    temp=temp//10
if(n==a):
    print("Armstrong number")
else:
    print("Not a armstrong number")
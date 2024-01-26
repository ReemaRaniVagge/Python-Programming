# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 17:41:44 2022

@author: amar
"""

a=int(input("enter the no to print prime numbers"))
print("prime numbers from 1 to",a)
for i in range(2,a+1):
    count=0
    for j in range(2,i//2+1):
        if(i%j==0):
            count=count+1
    if(count==0):
        print(i)
        
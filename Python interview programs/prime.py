# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 17:31:58 2022

@author: amar
"""



a=int(input("enter a no"))
count = 0
for i in range (2,a//2):
    if(a%i==0):
        count = count+1
    if(count==0):
        print("it is a prime no")
    else:
        print("not a prime no")
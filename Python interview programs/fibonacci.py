# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:06:06 2022

@author: amar
"""

a=int(input("enter the range of fibonaccci series"))
x=0
y=1
for i in range (a):
    if(i<=1):
        next=i
    else:
        next=x+y
        x=y
        y=next
print()
    
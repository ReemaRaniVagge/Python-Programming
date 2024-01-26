# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:47:36 2022

@author: amar
"""

year=int(input("enter the year"))

if((year%400==0) or ((year%4==0) and (year%100!=0))):
    print("leap year")
else:
    print("not a leap year")
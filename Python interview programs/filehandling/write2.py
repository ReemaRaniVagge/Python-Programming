# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:34:36 2023

@author: amar
"""

#now task is read all the data from myfile and write in abc file-its done below

f=open('myfile.txt','r')

f1=open('abcd','w')

for data in f:
    f1.write(data)
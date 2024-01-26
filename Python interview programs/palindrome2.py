# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:13:55 2022

@author: amar
"""

def check(str):
    rev=str[::-1]
    return "palindrome" if rev==str else "not a palindrome"
print(check(str))
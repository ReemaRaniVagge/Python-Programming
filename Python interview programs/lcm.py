# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:31:42 2022

@author: amar
"""

a=int(input("enter first number"))
b=int(input("enter second number"))
print()

if(a>b):
    maxi=a
else:
    maxi=b

while(True):
    if(maxi%a==0 and maxi%b==0):
        print("Lcm of {0} and {1} is{2}".format(a,b,maxi))
        break
    maxi +=1
print()

##################################################

def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b, a%b)
    
x = a
y = b
print("Hcf of {0} and {1} is {2}".format(a,b,hcf(a,b)))
print("LCM is ",(a*b)/hcf(a,b))
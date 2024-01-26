# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:26:10 2022

@author: amar
"""

a=int(input("enter no of rows"))
b=int(input("enter no of columns"))

print("Pattern1")

for i in range(a):
    for j in range (b):
        print("*" ,end=" ")
    print()
print("Pattern2")

for i in range (a):
    for j in range(b):
        print(i,end=" ")
    print()
print("pattern3")

for i in range (a):
    for j in range(b):
        print(j,end=" ")
    print()
print("pattern4")

for i in range(0,a):
    for j in range(i):
        print(i,end=" ")
    print()
print("pattern 5")

for i in range(0,a):
    for j in range(i):
        print("@",end=" ")
    print()
print("pattern 6")

for i in range(0,a):
    for j in range(i):
        print(j,end=" ")
    print()
print("pattern 7")

for i in range (a,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    
print("pattern 8")

for i in range (a,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()
    
print("pattern 9")

for i in range (a,0,-1):
    for j in range(i):
        print(j,end=" ")
    print()
    
print("pattern 10")

for i in range (a,0,-1):
    for j in range(i):
        print(a,end=" ")
    print()
    
print("pattern 11")

for i in range (a):
    for j in range(i):
        print(a,end=" ")
    print()
    
print("pattern 12")

c=0
for i in range(a,0,-1):
    c+=1
    for j in range(i):
        print(c,end=" ")
    print()
print("Pattern 13")

for i in range(a):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    
print("Pattern 14")

c=0
for i in range(a):
    for j in range(i):
        c+=1
        print(c,end=" ")
    print()
print("Pattern 15")

c=0
for i in range(1,a):
    c=c+i
    d=c
    for j in range(i):
        print(d,end=" ")
        d=d-1
    print()

print("Pattern16")

for i in range(1,a):
    for j in range(1,i):
        print(j,end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    
print("Pattern 17")

for i in range(a,0,-1):
    for j in range(a,a-i,-1):
        print(j,end=" ")
    for j in range(a-i+1,a+1):
        print(j,end=" ")
    print()
print("Pattern18")

for i in range(1,a+1):
    c=a
    for j in range(i):
        print(c*2,end=" ")
        c=c-1
    print()
print("Pattern 19")

for i in range(a+1):
    for j in range(i+1):
        print(i*j,end=" ")
    print()
print("Pattern20")

for i in range(2*a):
    for j in range((i+1//2)):
        if(i%2!=0):
            print(i,end=" ")
        print(end=" ")
    if (i%2!=0):
        print()

print("Pattern 21")

for i in range(a+1):
    for j in range(a,0,-1):
        if(j>1):
            print(" ",end= " ")
        else:
            print(i,end=" ")
    print()
    
print("Pattern22")


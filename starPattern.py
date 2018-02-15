# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:44:55 2018

@author: lokesh.r
"""

"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
rep = int(input("enter input value = "))
for i in range(rep) :
    for j in range(i+1,0,-(i+1)):
        print(j*"* ")
for k in range(rep-1,0,-1) :
    for l in range(k,0,-(k+1)):
        print(l*"* ")


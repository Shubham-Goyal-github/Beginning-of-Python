# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 08:17:44 2021

@author: hp
"""

def gcd(a,b):
    if b==0:
        return
    return gcd(b,a%b)
print(gcd(4,8))

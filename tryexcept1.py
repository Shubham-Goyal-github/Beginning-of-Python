# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:04:36 2020

@author: hp
"""

s=input("enter score")
try:
    s=float(s)
    if s<0:
        print("not in a range")
    if s>1:
        print("not in a range")

    elif s>=0.9:
                print("a")
    elif s>=0.8:
                print("b")
    elif s>=0.7:
                print("c")
    elif s>=0.6:
                print("d")
    elif s<0.6:
                    print("f")
                    
except:
                        print("enetr a numeric value")
                        
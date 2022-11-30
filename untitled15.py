# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:07:23 2020

@author: hp
"""

data='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos=data.find('@')
print(atpos)
sppos=data.find(' ',atpos)
print(sppos)
host=data[0:4]
print(host)

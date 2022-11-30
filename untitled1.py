# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:30:08 2021

@author: hp
"""
import time
user_input=int(input("Enter the Time in Seconds"))

print("Time Format = Minutes:Seconds")
      


def countdown(t):
    while t>0:
        minutes,seconds=divmod(t,60)
        timer='{:02d}:{:02d}'.format(minutes,seconds)
        
        t-=1
        print(timer)
        time.sleep(1)
        
        
countdown(user_input)
print("Your TIME is Up")



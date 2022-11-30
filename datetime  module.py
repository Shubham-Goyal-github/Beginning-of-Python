# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:07:27 2020

@author: hp
"""
import datetime

#create some dates
print("creating dates")
print("""""""""""""""""""")

date1=datetime.date(1999,12,31)
date2=datetime.date(2000,1,1)
date3=datetime.date(2016,4,15)
#date4=datetime.date(2012,8,32)


#todays date
today=datetime.date.today()
print(today)
print(date1)
print(date2)
print(date3)

print("")

#compare dates
print("cmparing dates")
print('''''''''''''''''''''''')
print(date1 < date2)
print(date3<= date1)
print(date2 == date3)
print('')


#subtracting dates
print("subtarcting dates")
print("""""""""""""")
diff=date2-date1
print(diff)
print(diff.days)

diff2=date3-date2
print(diff2)
print(diff2.days)

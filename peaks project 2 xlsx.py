# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:01:33 2021

@author: hp

"""
#20BEE0073
import matplotlib.pyplot as plt
import pandas as pd
import numpy 
df2=pd.read_excel("breathe.xlsx")

amp=list(df2['Amplitude'])
time=list(df2['Timestamp'])
plt.plot(time,amp)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude(v)')
plt.title("Peaks and Valley Signal")

diff=list()
peak=[]
valley=[]
t=[]
t1=[]
diff.append(0)

length=len(amp)
for count1 in range(1,length):
   
    diff.append((amp[count1])-(amp[count1-1]))
    
for count in range(1,length):
    c=diff[count]
    d=diff[count-1]
    if numpy.sign(c)!=numpy.sign(d):
        if numpy.sign(diff[count])<0:
            peak.append(amp[count-1])
            t.append(time[count-1])
            
        elif numpy.sign(diff[count])>0:
            t1.append(time[count-1])
            valley.append(amp[count-1])
 
 
plt.plot(t,peak,"rs")          
plt.plot(t1,valley,"bo")
plt.show()

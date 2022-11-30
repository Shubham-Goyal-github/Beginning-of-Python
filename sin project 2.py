# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 09:26:33 2021

@author: hp
"""
#20BEE0073 SHUBHAM GOYAL
import numpy as np
import matplotlib.pyplot as plt
f=int(input('enter the frequency in hertz'))
omega=2*f*np.pi
x=np.arange(0,1/(1*np.pi),0.0001)
a=np.sin(omega*x)
b=np.cos(omega*x)
plt.figure()
plt.subplot(211)
plt.plot(x,a)
plt.xlabel("time")
plt.ylabel("sinwt")
plt.subplot(212)
plt.plot(x,b,'r')
plt.xlabel("time")
plt.ylabel("coswt")
plt.show()

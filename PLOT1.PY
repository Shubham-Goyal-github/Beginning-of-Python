import matplotlib.pyplot as plt
'''
a=[1,2,3,4,5,6,7,8,9,10] 
b=[.7,1.2,3,.4,2,1,.32,.7,.98,1]

plt.plot(a,b)
plt.ylabel('voltage(V)')

plt.xlabel('current(A)')
plt.axis([0,15,0,10])
plt.show()
plt.bar(a,b)
plt.show()

plt.plot(a,a,'r--')
b=[]
c=[]

for i in a:
    b.append(i**2)
    c.append(i**3)
    plt.plot(b,c)
'''
import pandas as pd
df2=pd.read_excel("breathe.xlsx")
print(df2)
a=list(df2['Amplitude'])
b=list(df2['Timestamp'])
plt.plot(b,a)

plt.xlabel('time(s)')
plt.ylabel("amplitude(v)")
plt.show()
breathe=a[0:1201]
plt.figure()
plt.plot(breathe)





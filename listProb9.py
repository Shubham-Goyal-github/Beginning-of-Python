r=[]
r=input("enter a list which is tobe reversed")
i=len(r)-1
s=[]
while i>=0:
       s.append(r[i])
       i=i-1
print('original list',r)
print('reversed list',s)

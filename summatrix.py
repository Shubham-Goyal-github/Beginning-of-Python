r=int((input("enter the row no.")))
c=int((input('enter the column no.')))
arr1=[]
arr2=[]
arr3=[]

for i in range(r):
    sub=[]
    for j in range(c):
     sub.append(int(input()))
    arr1.append(sub)

for i in range(r):
    sub=[]
    for j in range(c):
     sub.append(int(input()))
    arr2.append(sub)
    
for i in range(r):
    s=[]
    for j in range(c):
        s.append(int(arr1[i][j]+int(arr2[i][j])))
    arr3.append(s)
    
for i in range(r):
    for j in range(c):
        print(arr3[i][j],end=" ")
    print()
    
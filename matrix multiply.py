
arr1=[]
arr2=[]
arr3=[]

r1=int((input("enter the row no. for 1st matrix")))
c1=int((input('enter the column no.for 1st matrix"')))
print("enter 1st matrix elemnts")
for i in range(r1):
    sub=[]
    for j in range(c1):
     sub.append(int(input()))
    arr1.append(sub)
r2=int((input("enter the row no. for 2nd matrix")))
c2=int((input('enter the column no.for 2nd matrix"')))

print('enter the 2nd matrix elements')
for i in range(r2):
    sub=[]
    for j in range(c2):
     sub.append(int(input()))
    arr2.append(sub)

def multiply(r,c):
    x,s=0,0
    while x<c1:
        s+=(int(arr1[r][x]))*(int((arr2[x][c])))
        x+=1
    return(s)
if c1==r2:
    for i in range(r1):
        t=[]
        for j in range(c2):
            z=multiply(i,j)
            t.append(z)
        arr3.append(t)
    print(arr3)
else:
    print("matrix multiplication is not possible")
    
    
    
    

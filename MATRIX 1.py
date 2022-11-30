row=input('enter rows')
col=input('enter column')
print(row,col)
arr=[]
for i in range(int(row)):
    sub=[]
    for j in range(int(col)):
        sub.append(int(input()))
    arr.append(sub)
        
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=" ")
    print()
    
        
print(len(arr))



#20BEE0073 SHUBHAM GOYAL
import pandas as pd
df=pd.read_excel('Marks.xlsx')
le=df['Marks']

count=0
marks_list=df['Marks'].values.tolist()
names_list=df['Student Name'].values.tolist()

n=len(marks_list)
for i in range(n-1):
        
        for j in range(0,n-i-1):
            count=count+1
            if marks_list[j]>marks_list[j+1]:
                temp=marks_list[j+1]
                marks_list[j+1]=marks_list[j]
                marks_list[j]=temp
                temp2=names_list[j+1]
                names_list[j+1]=names_list[j]
                names_list[j]=temp2
print(marks_list)
print("first three rankers marks are")
print(marks_list[32],names_list[32])
print(marks_list[31],names_list[31])
print(marks_list[30],names_list[30])
l=0

u=len(marks_list)-1
mid=0
n=12
temp=0
index_12=0
while(l<=u):
    mid=(l+u)//2
    if marks_list[mid] == n:
            temp=1
            index_12=mid
            
            break
            
    else:
            if n > marks_list[mid]:
                l=mid+1
            else:
                u=mid-1
                
if temp==1:
    print('12 marks are scored by')
    print(names_list(index_12))
    
    
    

    
    
    
    

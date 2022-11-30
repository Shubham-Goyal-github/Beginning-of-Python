def binary_search(arr):
    l=0
    u=len(arr)-1
    mid=0
    
    while(l<=u):
        mid=(l+u)//2
        if arr[mid] == n:
            
            break
        else:
            if n > arr[mid]:
                l=mid+1
            else:
                u=mid-1
           
    
n=58
ar=[12,13,14,15,16,20,45,49,58,100]
(binary_search(ar))



t=-1
def linear_search(arr):
    global t
    for i in range(len(arr)):
        if arr[i]==n:
          t=1 
          break
        
            
linear_search(ar)  
if t==1:
  print("f")
else:
  print("NF")

#RECURSIVE BINARY SEARCH
def bin(arr,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return bin(arr, low,mid-1, x)
        else:
            return bin(arr, mid+1, high, x)
    else:
        return -1
arr=[2,3,4,10,40]
x=10
result=bin(arr, 0, len(arr)-1, x)
if result==-1:
    print("not presenrt")
else:
    print("presrsnt")
    
    
    
    
    
    
    
    
    
    
    
    

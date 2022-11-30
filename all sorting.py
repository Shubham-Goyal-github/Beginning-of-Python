def bubblesort(arr):#right part gets sorted
    n=len(arr)
    count=0
    #traverse through all elements of array
    for i in range(n-1):
        #range(n) aslo work but outer loop will repaet 1 more time
        #lAst i elements are already in place
        for j in range(0,n-i-1):
            count=count+1
            if arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    print(count)
    
def insertion_sort(arr):#left part gets sorted
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        else:
            arr[j+1]=key
    print(arr)
def selectio_sort(arr):
    
    for i in range(len(arr)):
            min_idx=i
            for j in range(i+1,len(arr)):
                if arr[min_idx]>arr[j]:
                    min_idx=j
            temp=arr[i]
            arr[i]=arr[min_idx]#swapping with the element with which we started
            arr[min_idx]=temp
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

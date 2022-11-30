try:
    arr=[]
    arr_trans=[]
    arr3=[]
    

    r=int((input("enter the row no. for matrix")))
    c=int((input('enter the column no.for matrix')))
    if r==c:
        print('Enter the matrix elements')
        
        for i in range((r)):
            sub=[]
            for j in range((c)):
                sub.append(int(input()))
            arr.append(sub)
        
    def trace(input_matrix):
        t=0
        
        for i in range(0,r):
            t+=(int(input_matrix[i][i]))
        return (t)
    trace_value=trace(arr)
    
    def multiply(r,c):
        x,s=0,0
        while x<c:
            s+=(int(arr[r][x]))*(int((arr_trans[x][c])))
            x+=1
        return(s)

   
    for i in range(r):
        w=[]
        for j in range(c):
                w.append(arr[j][i])
        arr_trans.append(w)
      
    for i in range(r):
            t=[]
            for j in range(c):
                z=multiply(i,j)
                t.append(z)
            arr3.append(t)
    def orthogonal_check(input_matrix):
        
        for i in range(r):
                for j in range(c):
                    if r==c:
                        if input_matrix[i][j]==1:
                            return True
                        else:
                            return False
                    elif r!=c:
                        if input_matrix[i][j]==0:
                            return True
                        else:
                            
                            return False
                    
                    
        
         
    list_ans=[trace_value,orthogonal_check(arr3)]
    print(list_ans)
    
            
                
  
        
        
            
except:
    print("Sorry!! You are giving an wrong input ")
    
    
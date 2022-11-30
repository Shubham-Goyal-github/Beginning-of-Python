f=open('F:\CSE 1001\word1.txt')
x=[]
for l in f:
    s=(l.split())
    for w in s:
        if w in x:
            continue
        x.append(w)
        
print(x.sort())

            
  

     
 
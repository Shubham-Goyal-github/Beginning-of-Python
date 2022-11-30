def replace(l,x,y):
    for i in range(len(l)):
        if l[i]==x:
            l[i]=y
    return l
lst=[]
lst=input("enter the list")
x1=int(input('enter the no. which is to be replaced'))
y1=int(input('enter the no. which is to be included'))
print(replace(lst,x1,y1))

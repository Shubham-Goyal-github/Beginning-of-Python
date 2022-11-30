def naturalNumber(s):
    i=1
    l=list()
    while i<=s:
        l.append(i)
        i+=1
    return l
try:
    


    n=int(input("enter the no.upto which you want the list of natural no.s"))


    print("the list of natural numbers till",n,'is',naturalNumber(n))
except:
    print('integer value is to be emtered only')
    
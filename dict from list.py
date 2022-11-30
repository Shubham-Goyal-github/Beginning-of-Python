'''
counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)
a=list()
b=tuple()

x=counts.get('shubham','not available')
print(x)

'''
counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name]=counts.get(name,0)+1#indexing in a list is from 0
print(counts)

'''a={'1':7,'2':[3,4],'1':5}
print(a)
'''
'''
b={'1':[1,2,3],'2':[3,4]}
del b['1'][1]
print(b)
b.clear()
print(b)
del b#b is deleted
'''

a={'1':[1,2,3],'2':[3,4]}
print(a)
print(a['1'])
a['1'].append((7))
print(a)
n=[]
n.append(a)
print(n)
print(a['1'])
print(a.items())
print(a.keys())
print(a.values())

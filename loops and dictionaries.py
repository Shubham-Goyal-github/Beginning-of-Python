counts={'chuck':1,'fred':42,'jan':100}
for key in counts:
    print(key,counts[key])
    
    
print(list(counts))
print(counts.values())
print(counts.keys())
print(counts.items())

for i,j in counts.items():
    print(i,j)
    
    
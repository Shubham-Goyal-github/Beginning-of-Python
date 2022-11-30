m=(222,28,5,37,5697813)
sma=None
for  i in m:
    if sma is None:
        sma=i
    if sma > i:
        sma=i
        
print("smallest no. is",sma)

    
    
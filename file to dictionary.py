counts=dict()
print("enter the line")
line=input(' ')
words=line.split()
print("words are as follows",words)

print('counting......')
for word in words:
    counts[word]=counts.get(word,0)+1
print("counts",counts)
print(counts.get('the'))
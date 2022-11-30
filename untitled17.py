path="F:\CSE 1001"
name=input('eneter file name')
fh=open(path+'\\'+name)
for line in fh:
     if line.startswith('From'):
        print(line)
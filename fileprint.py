path="F:\CSE 1001"
na=input('enter a file name')
inp=open(path+'\\'+na)
for line in inp:
        line=line.rstrip()
        print(line.upper())
             
f=open("D:\VIT VELLORE\CSE 1001\word2.txt")
ct=0
for l in f:
    l=l.rstrip()
    if l.startswith("From:"):
        continue
    if l.startswith("From"):
        
        ct=ct+1
        s=l.split()
        print(s[1])
print('There are ',ct,'lines in the file with\'From\' as the first word.')
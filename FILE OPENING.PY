fhand=open('D:\VIT VELLORE\CSE 1001\mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if line.startswith('From'):
        print(line)
    

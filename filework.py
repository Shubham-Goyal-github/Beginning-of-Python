fname=input("enter the file name")
try:
    fhand=open(fname)
    count=0
    for line in fhand:
        if line.startswith('Subject'):
           count+=1
    print('there was',count,'\'subject\' lines in ',fname)
except:
    print('wrong file name input',fname)
    
    
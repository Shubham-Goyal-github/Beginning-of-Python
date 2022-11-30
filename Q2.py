print("Hello!!Here you can calculate the compund interests on your investing value")
print("principal value",'   ',"rate of interest")
print("above1000",'        ','5%')
print("above2500",'        ','7%')
print("above5000",'        ','10%')
print("above10000",'       ','20%')
pv=(input('enter your principal amount'))
try:
    pv=int(pv)
    if pv<1000:
        rate=0
    elif  pv>=1000&pv<2500:
        rate=5
    elif pv>=2500&pv<5000:
        rate=7
    elif pv>=5000&pv<10000:
        rate=10
    else:
        rate=20
    c=input("In what mode you will enter the time period.Press M for months or press Y for years")
    if c =='M':
        tp=float(input('enter the time period'))
        tp=tp/12
        fv=pv*((1+rate)**tp)
        print("Rs",pv,"in",tp,"years of time period  at",rate," % of interest will be Rs",fv)
    elif c == 'Y':
        tp=float(input('enter the time period'))
    fv=pv*((1+rate)**tp)
    print("Rs",pv,"in",tp,"years of time period  at",rate," % of interest will be Rs",fv)
except:
        print("Oops!!you have entered a wrong input please enter an suitable alphabet")
print('thank you')

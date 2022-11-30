def f(x):
    y=-5*(x**5)+67*(x**2)-47
    return y
a=f(0)
b=f(1)
c=f(2)
d=f(3)
max=-1
for i in [a,b,c,d]:
    if max<i:
        max=i
print("maximum among",a,b,c,d,"is",max)

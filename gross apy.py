hours=input("enetr hours")
rateph=input("enter rate per hours")
hours=float(hours)
rateph=float(rateph)

if hours<=40:
    amt=(hours)*(rateph)
else:
    amt=(40*rateph)+((hours-40)*1.5*rateph)
print(amt)
temp ={}
print(temp)
print(type(temp))

d=dict()
print(d)
print(type(d))

temp={'RAM':'Lg','Rohan':'MI',"Sohan":'di'}
print(temp)

d['ram']=55
d['ramesh']=66
d['gfg']=33
print(d)

print(d.keys())
print(d.values())

print(d['ram'])

print(len(d))
del d['gfg']
print(d)
print('ram' in d)

print('rohit' in d)

m=dict(d)
print(m)


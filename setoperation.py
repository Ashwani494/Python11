marks={11,12,15,66,12}
print(marks)

marks.add(555)
print(marks)

marks.remove(12)
print(marks)

fruit=frozenset(['apple','mango'])
print(fruit)

#fruit.add('ss')

# this will create dictionary but not set
a={}
print(a)
print(type(a))
# set function creates an empty set
b=set()
print(b)
print(type(b))

b= set(marks) #copy
print(b)

p={1,2,3,4}
q={4,5,61,1}

#union
print(p|q)

#intersection

print(p&q)

#difference
print(p-q) #which are in a but not in b

#symmetric difference
print(p^q)

print(p)
print(p.clear())
print(p)


#memebership operator

print(15 in marks)

print(15 not in marks)

x= q.copy()
print(x)

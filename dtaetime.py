from time import *






# it gives the output since 1970 in seconds
print(time())
# it gives the output in tuple format
print(localtime(time()))

tup=(2019,7,21,9,49,25,6,201,0)
print(mktime(tup))

print(localtime(mktime(tup)))
print(asctime())





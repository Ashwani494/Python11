f=open("Koala.jpg","rb")
f2=open("bhola.jpg","wb")
for data in f:
    print(data)
    f2.write(data)
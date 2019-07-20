f=open("myfile1.txt","r")
f1=open("savefile.txt","w")

for data in f:
    print(data)
    f1.write(data)
'''s="welcome in Python"
print(s)
print(s[0:])
print(s[0::2])

print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.title())
print(s.swapcase())


print(len(s))
st=s.split()
for i in st:
    print(i)'''



'''str="Her name is tamana and tamana is good girl"
print(str)
x=input("enter u want to find")
if x.isdigit()==True:
    print("Item can not contain digit")
else:
    y=str.find(x)
    if y==-1:
        print("item not found")
    else:
        print("item found at location",y)
        rep = input("enter u want to  replace")
        st2=str.replace(x,rep)
        print(st2)'''


name="humtum"
print(name.isalpha())

stid="Bteup1234"
print(stid.isalnum())
x="                      dklsjldjflsjf           "
print(x,end="")
print("hi")
print(x.strip(),end="hello")
print()
print(x.lstrip(),end="hello")
print()
print(x.rstrip(),end="hello")
y="!!!!!!!!!!!! dklsjldjflsjf           "
print(y)
print(y.lstrip('!'))

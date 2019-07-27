from tkinter import *
root = Tk()
def ldata():
    res=l.curselection()
    #print(res)
    for item in res:
        print(l.get(item))


def deletedata():
    res = l.curselection()
    # print(res)
    for item in res:
        print(l.delete(item))


f=Frame(root)
scroll=Scrollbar(f)
scroll.pack(side=RIGHT,fill=Y)
l=Listbox(f,yscrollcommand=scroll.set,width=30,height=15,selectmode=SINGLE)
'''l.insert(1,"c++")
l.insert(3,"java")
l.insert(2,"python")'''
for i in range(111):
    l.insert(END,"Data"+str(i))

l.pack()

scroll.config(command=l.yview)
f.pack()
btn = Button(root, text="Get list data", command=ldata).pack()
btn1 = Button(root, text="delete list data", command=deletedata).pack()
mainloop()
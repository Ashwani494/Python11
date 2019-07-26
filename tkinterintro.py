from tkinter import *
root = Tk()


root.title("My First Gui")



p=StringVar()
lbl=Label(root,text="enter your name",fg="red",bg="yellow",font=("Times New Roman",25,"bold"),textvariable=p)

def getdata():
    x=y.get()
    p.set(x)

y=StringVar()
txt_name=Entry(root,justify="right",fg="red",bg="yellow",font=("Times New Roman",23,"bold"),textvariable=y).pack(side=RIGHT)
btn=Button(root,text="Click Me",fg="red",bg="yellow",command=getdata)
btn.pack()
lbl.pack(side=LEFT)
root.geometry("600x500+400+200")
#root.resizable(0,0)
mainloop()
from tkinter import *

root = Tk()

def get_check():
    print(i.get())
    print(j.get())


f=LabelFrame(root,text="select Language Known")
i=IntVar()
j=IntVar()
r1=Checkbutton(f,text="Hindi",variable=i)
r2=Checkbutton(f,text="English",variable=j)


r1.pack()
r2.pack()
f.pack()






btn = Button(root, text="Get checkbox value",command=get_check).pack()
root.geometry("400x500+120+120")
root.resizable(0, 0)
mainloop()

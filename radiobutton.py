from tkinter import *

root = Tk()

def get_radio():
    print(i.get())
    print(j.get())

f=LabelFrame(root,text="select Gender")
i=IntVar()
r1=Radiobutton(f,text="male",value=1,variable=i)
r2=Radiobutton(f,text="Female",value=2,variable=i)


r1.pack()
r2.pack()
f.pack()


ff=LabelFrame(root,text="select Caste")
j=IntVar()
r1=Radiobutton(ff,text="General",value=1,variable=j)
r2=Radiobutton(ff,text="OBC",value=2,variable=j)


r1.pack()
r2.pack()
ff.pack()



btn = Button(root, text="open new window",command=get_radio).pack()
root.geometry("400x500+120+120")
root.resizable(0, 0)
mainloop()

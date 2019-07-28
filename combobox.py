from tkinter import *
from tkinter.ttk import Combobox
def comboget():
    print(c.get())

root = Tk()
l=["GKP","LKO","NDLS"]
c=Combobox(root,values=l,height=2)
c.set("Select Your city")
c.pack()
btn = Button(root, text="combodata",command=comboget).pack()
root.geometry("400x500+120+120")
root.resizable(0, 0)
mainloop()

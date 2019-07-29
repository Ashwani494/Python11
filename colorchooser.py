from tkinter import *
from tkinter import colorchooser

def choosecolor():
    c=colorchooser.askcolor()
    print(c[1])
    root.configure(background=c[1])
root=Tk()
btn=Button(root,text="color",command=choosecolor).pack()
mainloop()
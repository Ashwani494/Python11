from tkinter import *
def msg(event=""):
    print("hello")

root=Tk()
root.bind("<Control-o>",msg)


btn=Button(root,text="Get Text area data",command=msg).pack()
mainloop()
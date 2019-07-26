from tkinter import *

class Mywindow:
    def msg(self):
        print("hi")

    def __init__(self,master):
        self.btn=Button(master,text="Click me",command=self.msg).pack()




root=Tk()
b=Mywindow(root)
root.title("My Calculator")
root.geometry("250x400+300+200")
root.resizable(0,0)

mainloop()
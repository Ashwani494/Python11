from tkinter import *

def msg():
    print("good Morning")


root = Tk()
root.title("My First Gui")
btn=Button(root,text="Click Me",fg="red",bg="yellow",command=msg)
btn.place(x=200,y=150)
root.geometry("600x500+400+200")
#root.resizable(0,0)
mainloop()
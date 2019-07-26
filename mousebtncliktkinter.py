from tkinter import *

def msg(event):
    print("good Morning")

def msg2(event):
    print("good afternoon")

def msg3(event):
    print("good evening")

root = Tk()

root.title("My First Gui")
btn=Button(root,text="left Click",fg="red",bg="yellow")
btn.bind("<Button-1>",msg)
btn.place(x=200,y=150)
btn1=Button(root,text="middle Click",fg="red",bg="yellow")
btn1.bind("<Button-2>",msg2)
btn1.place(x=200,y=300)
btn2=Button(root,text="right Click",fg="red",bg="yellow")
btn2.bind("<Button-3>",msg3)
btn2.place(x=200,y=450)
root.geometry("600x500+400+200")
#root.resizable(0,0)
mainloop()
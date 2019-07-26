from tkinter import *

root=Tk()
root.title("My Calculator")
header=Frame(root)
btn7=Button(header,text="7",font=("Ariel",12),bd=15).grid(row=0,column=0)
header.pack(side=TOP)


footer=Frame(root)
btn8=Button(footer,text="8",font=("Ariel",12),bd=15).grid(row=0,column=0)
footer.pack(side=BOTTOM)
root.geometry("250x400+300+200")
root.resizable(0,0)
mainloop()
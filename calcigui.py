from tkinter import *


root = Tk()

root.title("My First Gui")

'''display=Entry(root,bd=20,justify="right",font=("Ariel",12))
display.grid(row=0,columnspan=4)
btn7=Button(root,text="7",font=("Ariel",12),bd=15).grid(row=1,column=0)
btn8=Button(root,text="8",font=("Ariel",12),bd=15).grid(row=1,column=1)
btn9=Button(root,text="9",font=("Ariel",12),bd=15).grid(row=1,column=2)
btn_add=Button(root,text="+",font=("Ariel",12),bd=15).grid(row=1,column=3)

'''
txt=Entry(root,bd=12,font=("ARIEL",16,"bold"))
txt.grid(row=0,columnspan=3)
btn=Button(root,text="7",fg="red",bg="yellow",font=("ARIEL",14,"bold"),bd=6)
btn.grid(row=1,column=0)
btn1=Button(root,text="8",fg="red",bg="yellow",font=("ARIEL",14,"bold"),bd=6)
btn1.grid(row=1,column=1)
btn2=Button(root,text="9",fg="red",bg="yellow",font=("ARIEL",14,"bold"),bd=6)
btn2.grid(row=1,column=2)
root.geometry("400x500+400+200")
#root.resizable(0,0)
mainloop()
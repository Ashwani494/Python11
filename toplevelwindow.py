from tkinter import *
root = Tk()
def open_window():
    top=Toplevel()
    top.title("Top level window")
    top.geometry("400x500+120+120")
    btn = Button(top, text="close", command=top.destroy).pack()




btn=Button(root,text="open new window",command=open_window).pack()
root.geometry("400x500+120+120")
root.resizable(0,0)
mainloop()

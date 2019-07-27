from tkinter import *
from tkinter import messagebox
root=Tk()
def save():
    #result=messagebox.askyesno("Save Dialog box","Do you want to save this file")
    result = messagebox.showwarning("Save Dialog box", "Do you want to save this file")
    print(result)
    if result==True:
        print("file save ho gaya")
btn=Button(root,text="save file",command=save).pack()
mainloop()
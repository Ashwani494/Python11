from tkinter import *
from tkinter import simpledialog
root=Tk()
def inputdata():
    for i in range(4):
        s=simpledialog.askstring("student marks","enter student marks")
        print(s)


btn=Button(root,text="get marks",command=inputdata).pack()
mainloop()
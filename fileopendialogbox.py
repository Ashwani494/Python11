from tkinter import *
from tkinter import filedialog

root=Tk()

def open_file():
    result=filedialog.askopenfile(initialdir="/",title="Open file",
              filetypes=(("Text Document","*.txt"),("All Files","*.*")))

    print(result)
    for data in result:
        print(data)

btn=Button(root,text="Openfile",command=open_file).pack()
mainloop()
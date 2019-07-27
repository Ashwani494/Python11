from tkinter import *

root=Tk()
def spin_get():
    print(spin.get())
    print(s.get())

    
s=Scale(root,from_=200,to=10,orient=VERTICAL,length=100,width=10,sliderlength=50)
s.set(50)

s.pack(side=RIGHT,fill=Y)

spin=Spinbox(root,from_=1,to=4)
spin.pack()
btn=Button(root,text="Get spin",command=spin_get).pack()
mainloop()
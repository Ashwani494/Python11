from tkinter import *
from tkinter.font import *
root=Tk()
def get_data():
    print(y.get())
    print(txt_area.get(1.0,END))

def get_selected_data():
    result=txt_area.selection_get()
    print(result)

def get_selected_data_pos():
    result=txt_area.selection_get()
    pos=txt_area.search(result,1.0,stopindex=END)
    print(pos)

def clear():
    txt_area.delete(1.0,END)

my_font=Font(family="Times New Roman",size=24,weight="bold",
             underline=1,slant='italic',overstrike=1)
root.title("My Notepad")
y=StringVar()
z=StringVar()
txt_area=Text(root,width=25,height=6,padx=5,
              pady=5,wrap=WORD,selectbackground="red",bd=2,insertwidth=3,font=my_font)
txt_area.insert(INSERT,"hello how r you")
txt_area.pack(fill=BOTH,expand=1)
txt=Entry(root,textvariable=y).pack()
btn=Button(root,text="Get Text area data",command=get_data).pack()
btn_selection=Button(root,text="Get selected Text area data",command=get_selected_data).pack()
btn_selection_pos=Button(root,text="Get selected Text area data position",command=get_selected_data_pos).pack()
btn_clear=Button(root,text="khali karo",command=clear).pack()
root.geometry("500x500+300+100")
#root.resizable(0,0)
mainloop()
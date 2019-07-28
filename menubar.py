from tkinter import *
root = Tk()
def msg():
    print("file open ho gaya")
main_menu=Menu(root)
root.config(menu=main_menu)

file_menu=Menu(main_menu)
main_menu.add_cascade(label="FILE",menu=file_menu)
file_menu.add_command(label="New",command=msg)


edit_menu=Menu(main_menu)
main_menu.add_cascade(label="EDIT",menu=edit_menu)


root.geometry("400x500+120+120")
root.resizable(0, 0)
mainloop()

from tkinter import *

class Notepad:
    def msg(self):
        print("hi")

    def __init__(self,master):
       ''' main_menu = Menu(root)
        root.config(menu=main_menu)

        file_menu = Menu(main_menu)
        main_menu.add_cascade(label="FILE", menu=file_menu)
        file_menu.add_command(label="New", command=msg)

        edit_menu = Menu(main_menu)
        main_menu.add_cascade(label="EDIT", menu=edit_menu)
'''
       self.txt_area = Text(master,  padx=5, pady=5, wrap=WORD, selectbackground="red", bd=2, insertwidth=3)

       self.txt_area.pack(fill=BOTH, expand=1)
       self.master=master
       self.main_menu = Menu()
       self.master.config(menu=self.main_menu)
       # creating file menu
       self.file_menu = Menu(self.main_menu, tearoff=False)
       self.main_menu.add_cascade(label="File", menu=self.file_menu)
       # to add open in file menu
       self.file_menu.add_command(label="Open")
       self.file_menu.add_separator()
       self.file_menu.add_command(label="Save")
       self.file_menu.add_command(label="SaveAs")
       # seprator


root=Tk()
b=Notepad(root)




mainloop()
from tkinter import *
from tkinter import filedialog,messagebox

class Notepad:
    '''def msg(self):
        print("hi")'''
    current_file="no-file"
    def new_file(self):
        pass

    def open_file(self):
        result = filedialog.askopenfile(initialdir="/", title="Open file",
                                        filetypes=(("Text Document", "*.txt"), ("All Files", "*.*")))
        #print(result)
        for data in result:
            self.txt_area.insert(INSERT, data)
        self.current_file=result.name

    def save_file(self):
        if self.current_file=="no-file":
            self.saveas_file()
        else:
            f = open(self.current_file, mode="w")
            f.write(self.txt_area.get(1.0, END))
            f.close()



    def saveas_file(self):
        f=filedialog.asksaveasfile(mode='w',defaultextension="*.txt")
        data=self.txt_area.get(1.0,END)
        f.write(data)
        self.current_file = f.name
        f.close()

    def exit_file(self):
        s=self.txt_area.get(1.0, END)
        #print("a=",s)
        if self.current_file == "no-file" or s=="":
            quit()
        else:
            result = messagebox.askyesnocancel("Save Dialog box", "Do you want to save this file?")
            if result==True:
                self.saveas_file()
            elif result==False:
                quit()


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
       self.file_menu.add_command(label="New", command=self.new_file)
       # to add open in file menu
       self.file_menu.add_command(label="Open",command=self.open_file)
       self.file_menu.add_separator()
       self.file_menu.add_command(label="Save",command=self.save_file)
       self.file_menu.add_command(label="SaveAs",command=self.saveas_file)
       self.file_menu.add_command(label="Exit", command=self.exit_file)
       # seprator


root=Tk()
b=Notepad(root)




mainloop()
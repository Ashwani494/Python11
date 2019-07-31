from tkinter import *
from tkinter import messagebox
import pymysql
taz=Tk()

############### database conncetion #########################
def dbconfig():
    global mycursor,conn
    conn = pymysql.connect(host="localhost", user="root", db="wahtaz")
    mycursor = conn.cursor()

#########################remove all widgets from screen #################

def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()
#############################################################
def mainheading():
    label = Label(taz, text="Hotel WahTaz Management system", bg="yellow", fg="green",
                  font=("Comic Sans Ms", 24, "bold"), padx=60)
    label.grid(row=0, columnspan=5)


############  login action ##################
def adminlogin():
    dbconfig()
    username=usernameVar.get()
    password=passwordVar.get()
    que="select * from user_info where userid=%s and password=%s"
    val=(username,password)
    mycursor.execute(que,val)
    data = mycursor.fetchall()
    flag = False
    for row in data:
        flag = True

    conn.close()
    if flag == True:
        welcomewindow()

    else:
        messagebox.showerror("Invalid User Credential",'either User Name or Password is incorrect')
        usernameVar.set("")
        passwordVar.set("")
############# def logout ########################
def logout():
    remove_all_widgets()
    mainheading()
    loginwindow()

################## add item window ##################
def additem():
    pass

################ bill generation ###################

def bill():
    pass


###################################################
usernameVar = StringVar()
passwordVar = StringVar()

def loginwindow():
    usernameVar.set("")
    passwordVar.set("")
    loginLabel = Label(taz, text="Admin Login", font="Arial 30")
    loginLabel.grid(row=1, column=2, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username")
    usernameLabel.grid(row=2, column=2, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password")
    passwordLabel.grid(row=3, column=2, padx=20, pady=5)

    usernameEntry = Entry(taz, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=3, padx=20, pady=5)

    passwordEntry = Entry(taz, show="*", textvariable=passwordVar)
    passwordEntry.grid(row=3, column=3, padx=20, pady=5)

    loginButton = Button(taz, text="Login", width=20, height=2, fg="green", bd=10, command=adminlogin)
    loginButton.grid(row=4, column=2, columnspan=2)

########## Welcome Window#######################
def welcomewindow():
    remove_all_widgets()
    mainheading()
    welcomeLabel = Label(taz, text="Welcome User", font="Arial 30")
    welcomeLabel.grid(row=1, column=1, padx=(50, 0), columnspan=3, pady=10)

    additemButton = Button(taz, text="Add Item", width=20, height=2, fg="green", bd=10, command=additem)
    additemButton.grid(row=3, column=0, columnspan=2)

    billButton = Button(taz, text="Bill Generation", width=20, height=2, fg="green", bd=10, command=bill)
    billButton.grid(row=3, column=2, columnspan=2)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=3, column=4, columnspan=2)

###############################################

taz.title("Hotel WAhTaz Managment System")
mainheading()
loginwindow()
taz.geometry("900x600+120+50")
mainloop()
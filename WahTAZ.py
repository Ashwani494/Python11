from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from  datetime import datetime
from tkinter.ttk import Combobox
taz=Tk()

# ========mainTreeView======================
tazTV = ttk.Treeview(height=10, columns=('Item Name''Rate','Type'))

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
############# validation ######################
def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

def only_char_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isalpha() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False
callback = taz.register(only_char_input)  # registers a Tcl to Python callback
callback1 = taz.register(only_numeric_input)  # registers a Tcl to Python callback
############# def logout ########################
def logout():
    remove_all_widgets()
    mainheading()
    loginwindow()
############## back buttton #####################

def backbutton():
    remove_all_widgets()
    mainheading()
    welcomewindow()
################ ondouble click get data ##############
def OnDoubleClick(event):
    item = tazTV.selection()
    itemNameVar1 = tazTV.item(item, "text")
    item_detail = tazTV.item(item, "values")

    itemnameVar.set(itemNameVar1)
    itemrateVar.set(item_detail[0])
    itemTypeVar.set(item_detail[1])
##########update item #####################
def updateItem():
    name = itemnameVar.get()
    rate = itemrateVar.get()
    type = itemTypeVar.get()
    dbconfig()
    query="update itemlist set item_rate=%s,item_type=%s where item_name=%s"
    val=(rate,type,name)
    mycursor.execute(query,val)
    conn.commit()
    messagebox.showinfo("Update Data", 'Item Updated Successfully')
    itemnameVar.set("")
    itemrateVar.set("")
    itemTypeVar.set("")
    getItemInTreeView()


##########delete item #####################
def deleteItem():
    name = itemnameVar.get()
    rate = itemrateVar.get()
    type = itemTypeVar.get()
    dbconfig()
    query = "delete from itemlist where item_name=%s"
    val = (name)
    mycursor.execute(query, val)
    result=messagebox.askyesno("Delete Dialog box","Do you want to Delete this Item")
    if result == True:
        conn.commit()
        messagebox.showinfo("Delete Data", 'Item Deleted Successfully')
    else:
        pass
    itemnameVar.set("")
    itemrateVar.set("")
    itemTypeVar.set("")
    getItemInTreeView()


############ get Item in tree view ###############
def getItemInTreeView():
    # to delete already inserted item
    records = tazTV.get_children()

    for element in records:
        tazTV.delete(element)

    # insert data in treeview
    conn = pymysql.connect(host="localhost", user="root", db="wahtaz")
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "select * from itemlist"
    mycursor.execute(query)
    data = mycursor.fetchall()

    for row in data:
        tazTV.insert('', 'end', text=row['item_name'], values=(row["item_rate"], row["item_type"]))
    conn.close()
    tazTV.bind("<Double-1>", OnDoubleClick)
############### get combo value ################
'''def comboget():
    return (itemType.get())'''

################# add item into database#########################
def additem():
    additemwindow()
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemTypeVar.get()
    print(name,rate,type)
    dbconfig()
    query = "insert into itemlist (item_name,item_rate,item_type) values(%s,%s,%s);"
    val = (name,rate,type)
    mycursor.execute(query,val)
    conn.commit()
    messagebox.showinfo("Save Data", 'Item Inserted Successfully')
    itemnameVar.set("")
    itemrateVar.set("")
    itemTypeVar.set("")
    getItemInTreeView()


################## add item window ##################
itemnameVar=StringVar()
itemrateVar=StringVar()
itemTypeVar=StringVar()

def additemwindow():
    remove_all_widgets()
    mainheading()

    itemnameLabel = Label(taz, text="ITEM DETAILS", font="Arial 30")
    itemnameLabel.grid(row=1, column=2, padx=(50, 0), columnspan=2, pady=10)

    ###############################
    billButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, command=backbutton)
    billButton.grid(row=1, column=0, columnspan=2)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=1, column=4, columnspan=2)

    ###########################

    itemnameLabel = Label(taz, text="Item name")
    itemnameLabel.grid(row=2, column=2, padx=20,  pady=5)


    itemrateLabel = Label(taz, text="Item Rate")
    itemrateLabel.grid(row=3, column=2, padx=20, pady=5)

    itemTypeLabel = Label(taz, text="Item Type")
    itemTypeLabel.grid(row=4, column=2, padx=20, pady=5)

    itemnameEntry = Entry(taz, textvariable=itemnameVar)
    itemnameEntry.grid(row=2, column=3, padx=20, pady=5)
    itemnameEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

    itemrateEntry = Entry(taz, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=3, padx=20, pady=5)
    itemrateEntry.configure(validate="key", validatecommand=(callback1, "%P"))  # enables validation

    itemTypeEntry = Entry(taz, textvariable=itemTypeVar)
    itemTypeEntry.grid(row=4, column=3, padx=20, pady=5)
    itemTypeEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation
    '''global itemType
    #l = ["BreakFast", "Lunch", "Dinner"]
    itemType = Combobox(taz, values=l, height=2)
    itemType.set("Select Item type")
    itemType.grid(row=4, column=3, padx=20, pady=5)'''

    label = Label(taz)
    label.grid(row=5, column=2, padx=20, pady=5)

    additemButton = Button(taz, text="Add Item", width=20, height=2, fg="green", bd=10,command=additem)
    additemButton.grid(row=6, column=0, columnspan=2)

    updateButton = Button(taz, text="UpDate Item", width=20, height=2, fg="green", bd=10, command=updateItem)
    updateButton.grid(row=6, column=2, columnspan=2)

    deleteButton = Button(taz, text="Delete Item", width=20, height=2, fg="green", bd=10,command=deleteItem)
    deleteButton.grid(row=6, column=4, columnspan=2)

    ###############################################
    tazTV.grid(row=7, column=2, columnspan=3)

    scrollBar = Scrollbar(taz, orient="vertical", command=tazTV.yview)
    scrollBar.grid(row=7, column=4, sticky="NSE")

    tazTV.configure(yscrollcommand=scrollBar.set)

    tazTV.heading('#0', text="Item Name")
    tazTV.heading('#1', text="Rate")
    tazTV.heading('#2', text="Type")

    getItemInTreeView()

########## option call back #################

def OptionCallBack(*args):
    global itemname
    itemname=combovariable.get()
    print(itemname)
    aa=ratelist()
    baserate.set(aa)
    global v
    for i in aa:
        for j in i:
            v = j



def OptionCallBack1(*args):
    global qty
    qty=qtyvariable.get()
    cost.set(0)
    finalvalue = int(v) * int(qtyvariable.get())
    cost.set(finalvalue)
################
def ratelist():
    dbconfig()
    que="select item_rate from itemlist where item_name=%s"
    val=(itemname)
    mycursor.execute(que,val)

    data = mycursor.fetchall()
    #print(data)
    return data
######## get data in combo box ###############

def combo_input():
    dbconfig()

    mycursor.execute('SELECT item_name FROM itemlist')

    data = []

    for row in mycursor.fetchall():
        data.append(row[0])

    return data
###########date time solution ##########
global x
x=datetime.now()

######### bill generation window #################

datetimeVar=StringVar()
datetimeVar.set(x)
customerNameVar=StringVar()
mobileVar=StringVar()
combovariable=StringVar()
baserate=StringVar()
qtyvariable=StringVar()
cost=StringVar()
def billgenerationwindow():
    remove_all_widgets()
    mainheading()

    itemnameLabel = Label(taz, text="BILL DETAILS", font="Arial 30")
    itemnameLabel.grid(row=1, column=1, padx=(50, 0), columnspan=3, pady=10)

    billButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, command=backbutton)
    billButton.grid(row=1, column=0, columnspan=2)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=1, column=4, columnspan=2)

    ##############################################
    dateTimeLabel = Label(taz, text="Date/Time")
    dateTimeLabel.grid(row=2, column=2, padx=20, pady=5)

    dateTimeEntry = Entry(taz, textvariable=datetimeVar)
    dateTimeEntry.grid(row=2, column=3, padx=20, pady=5)


    customerNameLabel = Label(taz, text="Customer Name")
    customerNameLabel.grid(row=3, column=2, padx=20, pady=5)

    customerNameEntry = Entry(taz, textvariable=customerNameVar)
    customerNameEntry.grid(row=3, column=3, padx=20, pady=5)
    customerNameEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enabl


    mobileLabel = Label(taz, text="Contact No")
    mobileLabel.grid(row=4, column=2, padx=20, pady=5)

    mobileEntry = Entry(taz, textvariable=mobileVar)
    mobileEntry.grid(row=4, column=3, padx=20, pady=5)
    mobileEntry.configure(validate="key", validatecommand=(callback1, "%P"))  # enables

    selectLabel = Label(taz, text="Select Item")
    selectLabel.grid(row=5, column=2, padx=20, pady=5)

    l=combo_input()

    c = ttk.Combobox(taz, values=l, textvariable=combovariable)
    c.set("Select Item")
    combovariable.trace('w', OptionCallBack)
    c.grid(row=5, column=3, padx=20, pady=5)
    ##########################################

    rateLabel = Label(taz, text="Rate ")
    rateLabel.grid(row=6, column=2, padx=20, pady=5)

    rateEntry = Entry(taz, textvariable=baserate)
    rateEntry.grid(row=6, column=3, padx=20, pady=5)

    quantityLabel = Label(taz, text="Quantity ")
    quantityLabel.grid(row=7, column=2, padx=20, pady=5)

    l2 = [1, 2, 3, 4, 5]
    qty = ttk.Combobox(taz, values=l2, textvariable=qtyvariable)
    qty.set("Select Quantity")
    qtyvariable.trace('w', OptionCallBack1)
    qty.grid(row=7, column=3, padx=20, pady=5)

    costLabel = Label(taz, text="Cost ")
    costLabel.grid(row=8, column=2, padx=20, pady=5)
    costEntry = Entry(taz, textvariable=cost)
    costEntry.grid(row=8, column=3, padx=20, pady=5)

    billButton = Button(taz, text="Bill Generation", width=20, height=2, fg="green", bd=10,
                        command=bill)
    billButton.grid(row=9, column=2, columnspan=2)
################ bill generation ###################

def bill():
    dt=datetimeVar.get()
    custname = customerNameVar.get()
    mobile=mobileVar.get()
    item_name=itemname
    itemrate = v
    itemqty= qtyvariable.get()
    total=cost.get()
    print(dt,custname,mobile,item_name,itemrate,itemqty,total)
    dbconfig()

    query = "insert into bill (datetime,customer_name,contact_no,item_name,item_rate,item_qty,cost) values(%s,%s,%s,%s,%s,%s,%s);"
    val = (dt,custname,mobile,item_name,itemrate,itemqty,total)
    mycursor.execute(query, val)
    conn.commit()
    messagebox.showinfo("Save Data", 'Bill Generated Successfully')
    customerNameVar.set("")
    mobileVar.set("")

    itemrateVar.set("")
    cost.set("")




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
    usernameEntry.configure(validate="key", validatecommand=(callback, "%P"))

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

    additemButton = Button(taz, text="Manage Restaurant", width=20, height=2, fg="green", bd=10, command=additemwindow)
    additemButton.grid(row=3, column=0, columnspan=2)

    billButton = Button(taz, text="Bill Generation", width=20, height=2, fg="green", bd=10, command=billgenerationwindow)
    billButton.grid(row=3, column=2, columnspan=2)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=3, column=4, columnspan=2)

###############################################

taz.title("Hotel WAhTaz Managment System")
mainheading()
loginwindow()

taz.geometry("900x600+120+50")
mainloop()
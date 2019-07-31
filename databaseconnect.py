import pymysql

# connection establish
conn=pymysql.connect(host="localhost",user="root",db="pythonrain")
mycursor=conn.cursor()
print("connection established")
'''query="create table techsrijan (Name varchar(20),age varchar(3))"'''
#ins="insert into techsrijan (Name,age) values('Ram','55')"
ins="update techsrijan set age='555' where Name='Ram'"
mycursor.execute(ins)
conn.commit() # to save the changes into database
print("table data inserted successfully")

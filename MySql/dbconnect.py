import mysql.connector as sql
mydb = sql.connect(host="localhost", user="root", password="Shiva@547")
print(mydb)
if(mydb):
    print("connection succesfull")
else:
    print("connection unsucessfull")

mycursor = mydb.cursor()

mycursor.excute("create Database Employee")
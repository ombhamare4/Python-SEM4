import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="EU1192003",database="Teachers")
'''
if (mydb):
    print("connected")
else:
    print("Something wrong")    
'''
mycursor = mydb.cursor()

mycursor.execute("Select name from info")

myresult = mycursor.fetchall()

for r in myresult:
    print(r)
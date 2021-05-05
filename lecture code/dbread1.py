import mysql.connector #step1

mydb=mysql.connector.connect(host="localhost",user="root",password="EU1192003",database="Teachers")

#Create database
mycursor = mydb.cursor()

mycursor.execute("Select name from info")

myresult=mycursor.fetchall()

for r in myresult:
    print(r)
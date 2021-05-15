#Om Ghashyam Bhamare SE DIV A 3
import mysql.connector #step1
mydb=mysql.connector.connect(host="localhost",user="root",password="EU1192003",database="Covid")
#Create database
mycursor = mydb.cursor()

sql="DELETE FROM users WHERE name='Might Guy'"
mycursor.execute(sql)

mycursor.execute("Select * from users ")

myresult=mycursor.fetchall()

for r in myresult:
    print(r)

mydb.commit()
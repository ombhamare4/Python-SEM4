import mysql.connector #step1
mydb=mysql.connector.connect(host="localhost",user="root",password="EU1192003",database="Teachers")
#Create database
mycursor = mydb.cursor()

sql="Update info set id=104 where name='Asuma'"
mycursor.execute(sql)

mycursor.execute("Select * from info")

myresult=mycursor.fetchall()

for r in myresult:
    print(r)

mydb.commit()
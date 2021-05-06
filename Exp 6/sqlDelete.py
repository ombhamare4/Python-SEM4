#Om Ghanshyam Bhamare Div: A Roll No:3
#Exp 6
import mysql.connector #step1
mydb=mysql.connector.connect(host="localhost",user="root",password="EU1192003",database="leafShinobi")
#Create database
mycursor = mydb.cursor()

sql="DELETE FROM INFO WHERE id=104"
mycursor.execute(sql)

mycursor.execute("Select * from info")

myresult=mycursor.fetchall()

for r in myresult:
    print(r)

mydb.commit()
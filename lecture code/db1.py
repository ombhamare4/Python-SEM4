import mysql.connector #step1

mydb=mysql.connector.connect(host="localhost",user="root",password="EU1192003",database="Teachers")

if (mydb):
    print("Connected...")
else:
    print("Something Wrong")

#Create database
mycursor = mydb.cursor()

mycursor.execute("CREATE database IF NOT EXISTS Teachers")
mycursor.execute("show databases")
for db in mycursor:
    print(db)

print("\n\nTables in database")
mycursor.execute("CREATE TABLE IF NOT EXISTS info(name TEXT,id INT)")
mycursor.execute("show tables")
for db in mycursor:
    print(db)


print("\n\nInsert")
# mycursor.execute("INSERT INTO info(name,id) values("Kakashi Hatake",121)")

sqlform="Insert into info(name,id) values(%s,%s)"

teacher=[("Kakashi",101),("Guy",102),("Asuma",103)]

mycursor.executemany(sqlform,teacher)

mydb.commit()


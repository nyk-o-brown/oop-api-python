import mysql.connector

mydb = mysql.connector.Connect(
    host="localhost",
    user="username",
    password="",
    database="yourdatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM your_table")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)





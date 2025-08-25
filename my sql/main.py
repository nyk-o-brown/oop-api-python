import mysql.connector

mydb = mysql.connector.Connect(
    host="localhost",
    user="username",
    password="",
    database="yourdatabase"
)

print(mydb.get_server_info())


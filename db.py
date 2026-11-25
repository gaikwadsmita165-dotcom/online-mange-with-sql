
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="online_shopping_db"
)

if mydb.is_connected():

    print("Database Connected Successfully")

else:

    print("Database Connection Failed")

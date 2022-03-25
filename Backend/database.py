import sys
import mysql.connector

main_list = sys.argv[1:]

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="myuser",
  password="mypassword",
  database="loan_management",
  port=3306,
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customer")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

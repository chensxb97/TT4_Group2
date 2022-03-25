import sys
import mysql.connector
import configparser

main_list = sys.argv[1:]
local_db_file = "local_db.txt"
config = configparser.ConfigParser()
config.read(local_db_file)

"""
login
signup
balance
currentloan
loanhistory
newloan
payloan
"""

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="myuser",
  password="mypassword",
  database="loan_management",
  port=3306,
)
mycursor = mydb.cursor()

if main_list[0] == "login":
    try:
        login_username = main_list[1]
        login_password = main_list[2]
        login_password_actual = config.get('user', login_username)
        if login_password == login_password_actual:
            print("True")
        else:
            print("False")
    except:
        print("False")

if main_list[0] == "signup":
    try:
        signup_username = main_list[1]
        signup_password = main_list[2]
        signup_name = main_list[3]
        signup_phone = main_list[4]
        signup_address = main_list[5]
        signup_balance = "0"
        mycursor.execute("SELECT * FROM customer")
        myresult = mycursor.fetchall()
        signup_id = str(len(myresult)+1)
        sql = "INSERT INTO customer (CustomerId, customer_name, customer_phone, customer_address, balance) VALUES (%s, %s,%s, %s,%s)"
        val = (signup_id, signup_name, signup_phone, signup_address, signup_balance)
        mycursor.execute(sql, val)
        config.set('userpassword',signup_username, signup_password)
        config.set('userid',signup_username, signup_id)
        with open(local_db_file, 'w') as configfile: 
            config.write(configfile)
        print("True")
    except:
        print("False")


if main_list[0] == "balance":
    balance_username = main_list[1]

if main_list[0] == "currentloan":
    currentloan_username = main_list[1]

if main_list[0] == "loanhistory":
    loanhistory_username = main_list[1]

if main_list[0] == "newloan":
    newloan_username = main_list[1]
    newloan_id = main_list[2]
    newloan_amount = main_list[3]

if main_list[0] == "payloan":
    payloan_username = main_list[1]
    payloan_id = main_list[2]
    payloan_amount = main_list[3]

import mysql.connector

dataBaseScript = "alx_book_store.sql"
host = "localhost"
user = "root"
password = "26627777"

try:
    with mysql.connector.connect(host=host, user=user, password=password) as myDataBase:
        pass
except:
    print("connection fail")
else:
    print("connection success \n")
try:
    with open(dataBaseScript, "r") as sqlScript:
        pass
except:
    print(f"can't open the file {dataBaseScript}")
else:
    print(f"file {dataBaseScript} open successfully")

# myCursor = myDataBase.cursor()
print(sqlScript.read())


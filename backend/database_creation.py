import mysql.connector

#installing credentials
host = "localhost"
user = "root"
password = "Joshua2001$"
database = "finalproj"

#connecting to the database
mydb = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

#setting cursor to execute queries
my_cursor = mydb.cursor()

#creating tables for data to be inserted
my_cursor.execute("SELECT * FROM css project")
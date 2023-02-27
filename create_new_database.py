import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="USERNAME",
    password="USER_PASSWORD",
    port='3306',
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS my_notes")
mycursor.execute("USE my_notes")
mycursor.execute('''
CREATE TABLE IF NOT EXISTS notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50),
    description VARCHAR(2000)
)
''')

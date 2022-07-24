# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    dataBase="sample")

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE sample")

# creating table
studentRecord = """CREATE TABLE StudentTable (
                   rollno int, 
                   name char, 
                   adress char
                   )"""

marksRecord = """CREATE TABLE MarksTable (
                   examid int,
                   rollno int, 
                   m1 int, 
                   m2 int, 
                   m3 int
                   )"""

# table created
cursorObject.execute(studentRecord)
cursorObject.execute(marksRecord)

# disconnecting from server
dataBase.close()

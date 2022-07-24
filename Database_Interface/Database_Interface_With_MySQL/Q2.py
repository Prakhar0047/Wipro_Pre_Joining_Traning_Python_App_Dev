import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="myusername",
    password="mypassword",
    database="mydatabase"
)

mycursor = mydb.mycursor()

mycursor.execute(
    "INSERT INTO StudentTable VALUES (1,'sagar','delhi')")

mycursor.execute(
    "INSERT INTO StudentTable VALUES (2,'suresh','banglore')")

mycursor.execute(
    "INSERT INTO StudentTable VALUES (3,'swmy','Hyd')")

mycursor.execute(
    "INSERT INTO StudentTable VALUES (4,'swati','chennai')")

mycursor.execute(
    "INSERT INTO MarksTable VALUES (1,1,12,23,23)")

mycursor.execute(
    "INSERT INTO MarksTable VALUES (2,2,23,34,34)")

mycursor.execute(
    "INSERT INTO MarksTable VALUES (3,3,23,12,34)")

mycursor.execute(
    "INSERT INTO MarksTable VALUES (4,4,21,31,21)")
mydb.commit()

import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()

cur.execute(
    "INSERT INTO StudentTable VALUES (1,'sagar','delhi')")

cur.execute(
    "INSERT INTO StudentTable VALUES (2,'suresh','banglore')")

cur.execute(
    "INSERT INTO StudentTable VALUES (3,'swmy','Hyd')")

cur.execute(
    "INSERT INTO StudentTable VALUES (4,'swati','chennai')")

cur.execute(
    "INSERT INTO MarksTable VALUES (1,1,12,23,23)")

cur.execute(
    "INSERT INTO MarksTable VALUES (2,2,23,34,34)")

cur.execute(
    "INSERT INTO MarksTable VALUES (3,3,23,12,34)")

cur.execute(
    "INSERT INTO MarksTable VALUES (4,4,21,31,21)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
import sqlite3
con = sqlite3.connect('example.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE StudentTable
               (rollno int, name char, adress char)''')

cur.execute('''CREATE TABLE MarksTable
               (examid int, rollno int, m1 int, m2 int, m3 int)''')

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
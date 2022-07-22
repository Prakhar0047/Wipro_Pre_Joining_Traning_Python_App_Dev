import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

# For Viewing
for row in cur.execute('SELECT name, (MarksTable.m1+MarksTable.m2+MarksTable.m3)/3 FROM StudentTable, MarksTable WHERE StudentTable.rollno = MarksTable.rollno'):
  print(row)

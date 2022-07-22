import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

# For Viewing
for row in cur.execute('SELECT * FROM StudentTable'):
  print(row)

for row in cur.execute('SELECT * FROM Markstable'):
  print(row)

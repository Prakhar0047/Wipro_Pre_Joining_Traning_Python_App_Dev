import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()
rollno = int(input())
name = input()
adres = input()
# cur.execute(
#     "INSERT INTO StudentTable VALUES (rollno,'name','adres') values(?,?,?)",(rollno,name,adres))
con.execute('insert into StudentTable(rollno, name, adress) values(?, ?, ?)',
             (rollno, name, adres))
con.commit()
con.close()
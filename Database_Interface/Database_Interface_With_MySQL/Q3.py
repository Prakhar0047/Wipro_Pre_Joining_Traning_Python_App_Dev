import MySQLdb

# connect python with mysql with your hostname,
# username, password and database
db = MySQLdb.connect("localhost", "root", "password", "sample")

# get cursor object
cursor = db.cursor()

# execute your query
cursor.execute("SELECT * FROM sample")

# fetch all the matching rows
result = cursor.fetchall()

# loop through the rows
for row in result:
    print(row)
    print("\n")

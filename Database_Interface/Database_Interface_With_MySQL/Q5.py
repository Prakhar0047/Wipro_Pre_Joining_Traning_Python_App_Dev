import mysql.connector
mytb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="sample")

cur = mytb.cursor()
count = 0
count1 = 0
while(1):
    print("Enter 1 for inertion into student table \nEnter 2 for insertion into marks table\nEnter 0 for  Exit")
    n = int(input())
    if n == 0:
        print("Program Exit with inserting rows")
        break
    elif n == 1:
        roolno = int(input("Eneter rool number: "))
        name = input("Enter name: ")
        adress = input("Enter adress: ")
        cur.execute("INSERT INTO StudentTable values({},\'{}\',\'{}\')".format(
            roolno, name, adress))
        count += 1
        print(count, "rows inserted sucessfully")
        mytb.commit()
    elif n == 2:
        examid = int(input("Eneter examid: "))
        rollno = int(input("Enter rollno: "))
        m1 = int(input("Enter m1: "))
        m2 = int(input("Enter m2: "))
        m3 = int(input("Enter m3: "))
        cur.execute("INSERT INTO MarksTable(EXAMID,ROLLNO,M1,M2,M3) VALUES(%s,%s,%s,%s,%s)",
                    (examid, rollno, m1, m2, m3))
        count1 += 1
        print(count1, "rows inserted sucessfully")
        mytb.commit()

cur.close()

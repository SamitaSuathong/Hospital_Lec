import pymysql
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="Hospital_Lec"
    )

inr1="INSERT INTO Request VALUES (4721, 1001, 2001, '2021-11-15', '17:00:00', 'Broken leg', 'Accepted');"
ina1="INSERT INTO Appointment VALUES (4821, 4721, 2001, 3001, 1001, '2021-11-20', '18:00:00', 'Surgery');"
inlr1="INSERT INTO Laboratory_Reservation VALUES (711, '91001', '2001', '1001', '4821', '2021-11-20', '15:00:00');"
inpr1="INSERT INTO Prescription VALUES (401, 3001, 2001, 4821, 'One pill for every meals');"

cursor=connection.cursor()

cursor.execute(inr1)
cursor.execute(ina1)
cursor.execute(inlr1)
cursor.execute(inpr1)

connection.commit()
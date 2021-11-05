import pymysql
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    )

db="CREATE database Hospital_Lec;"

cursor=connection.cursor()
cursor.execute(db)
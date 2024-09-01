import mysql.connector
conn=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="mansoorkhan",
    database="school"
)
cursor=conn.cursor()
print("List of databases: ")
cursor.execute("select * from student")
print(cursor.fetchall())
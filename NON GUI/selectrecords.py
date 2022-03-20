import mysql.connector as mysql
from mysql import connector
import mysql


conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
cursor = conn.cursor()
selectStudent = "select * from student"

cursor.execute(selectStudent)
result = cursor.fetchall()
conn.commit()
cursor.close()
print(result)

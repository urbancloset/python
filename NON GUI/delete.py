import mysql.connector
import mysql

conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
cursor = conn.cursor()
selectStudent = "select * from student"

cursor.execute(selectStudent)
result = cursor.fetchall()
print(result)
sid = input("Enter Id : ")
deleteStudent = "delete from student where Id = '"+sid+"'"

cursor.execute(deleteStudent)
conn.commit()
cursor.close()

import mysql.connector
import mysql
sid = input("Enter Id : ")

conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
cursor = conn.cursor()
deleteStudent = "delete from student where Id = '"+sid+"'"

cursor.execute(deleteStudent)
conn.commit()
cursor.close()

import mysql.connector
import mysql
name = input("Enter Name : ")
course = input("Enter Course : ")
semester = input("Enter Semester : ")

conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
cursor = conn.cursor()
insertStudent = "insert into student (name, course, semester) values (%s, %s, %s)"
values = (name, course, semester)
cursor.execute(insertStudent, values)
conn.commit()
cursor.close()

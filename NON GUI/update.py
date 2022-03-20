import mysql.connector
import mysql
sid = input("Enter Id : ")
name = input("Enter Name : ")
course = input("Enter Course : ")
semester = input("Enter Semester : ")

conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
cursor = conn.cursor()
updateStudent = "update student set name = '"+name+"', course='"+course+"', semester='"+semester+"' where Id = '"+sid+"'"

cursor.execute(updateStudent)
conn.commit()
cursor.close()

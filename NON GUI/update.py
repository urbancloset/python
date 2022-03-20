import mysql.connector
import mysql


conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
cursor = conn.cursor()
selectStudent = "select * from student"

cursor.execute(selectStudent)
result = cursor.fetchall()
print(result)
sid = input("Enter Id : ")
name = input("Enter Name : ")
course = input("Enter Course : ")
semester = input("Enter Semester : ")
updateStudent = "update student set name = '"+name+"', course='"+course+"', semester='"+semester+"' where Id = '"+sid+"'"

cursor.execute(updateStudent)
conn.commit()
cursor.close()

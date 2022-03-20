import mysql.connector
import mysql

conn = mysql.connector.connect(host="localhost", user="root", password="", database="Library")
cursor = conn.cursor()
viewBooks = "select * from book"
cursor.execute(viewBooks)
result = cursor.fetchall()
print(result)
conn.commit()
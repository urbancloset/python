import tkinter as tk
from tkinter import *
from tkinter import messagebox
from turtle import st
import mysql.connector
import mysql
from PIL import ImageTk, Image
import webbrowser
from tkinter import filedialog



root = tk.Tk()
root.title("Update Student Data")
root.attributes("-fullscreen", True)
root.geometry("2000x1500")

# Label(root, image=image).place(x=0, y=0, relheight=1, relwidth=1)

header = Frame(root, bg="#FFBB00", bd=5)
header.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)
headerlabel = Label(header, text="UPDATE STUDENT DATA", bg="black", fg="white", font=("Courier", 35, "bold"))
headerlabel.place(relx=0, rely=0, relwidth=1, relheight=1)

labelFrame = Frame(root, bg='black')
labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

lb2 = Label(labelFrame, text="Student ID  ", bg='black', fg='white', font=("Helvetica bold", 15))
lb2.place(relx=0.03, rely=0.11)
bookId = Entry(labelFrame)
bookId.place(relx=0.2, rely=0.11, relwidth=0.50, relheight=0.08)
Label(labelFrame, text="Name  ", font=("Helvetica bold", 15), bg="black", fg="white").place(relx=0.03, rely=0.4, relheight=0.08)
                      
StudentName = Entry(labelFrame)
StudentName.place(relx=0.2, rely=0.4, relwidth=0.50, relheight=0.08)

Label(labelFrame, text="RollNo  ", font=("Helvetica bold", 15), bg="black", fg="white").place(relx=0.03, rely=0.5, relheight=0.08)
StudentNRollno = Entry(labelFrame)
StudentNRollno.place(relx=0.2, rely=0.5, relwidth=0.50, relheight=0.08)
Label(labelFrame, text="Standard  ", font=("Helvetica bold", 15), bg="black", fg="white").place(relx=0.03, rely=0.6, relheight=0.08)
StudentStd = Entry(labelFrame)
StudentStd.place(relx=0.2, rely=0.6, relwidth=0.50, relheight=0.08)


def update():
        
    bid = bookId.get()
    name = StudentName.get()
    roll = StudentNRollno.get()
    std = StudentStd.get()
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="Student")
        cursor = conn.cursor()
        sql = "update StudentInfo set Name = '"+name+"', Rollno = '"+roll+"',Standard = '"+std+"' where Id = '"+bid+"'"
        cursor.execute(sql)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

def viewBooks():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="Student")
    cursor = conn.cursor()

    bid = bookId.get()

    books = "select Id, Name,Rollno,Standard from StudentInfo where Id='" + bid + "'"
    cursor.execute(books)

    if books is not None:
        for i in cursor:
            Label(labelFrame,
            text="%-15s%-25s%-35s%-45s" % (i[0], i[1],i[2],i[3])
                  , bg="black", fg="white", font=("Helvetica bold", 12)).place(relx=0.3, rely=0.3)
            conn.commit()
            cursor.close()
    else:
        pass

selectBtn = Button(labelFrame, text="Select Book", command=viewBooks)
selectBtn.place(relx=0.4, rely=0.2, relwidth=0.18, relheight=0.08)

UpdateBtn = Button(labelFrame, text="SUBMIT", bg='#d1ccc0', font=("times new roman", 15, "bold"), fg='black'
                       , command=update)
UpdateBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

quitBtn = Button(labelFrame, text="QUIT", bg='#f7f1e3', fg='black', font=("times new roman", 15, "bold")
                     , command=root.destroy)
quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
root.mainloop()


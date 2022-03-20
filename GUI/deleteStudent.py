import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import mysql
from PIL import ImageTk, Image
import webbrowser
from tkinter import filedialog


root = tk.Tk()
root.title("DELETE STUDENT DATA")
root.attributes("-fullscreen", True)
root.geometry("2000x1500")
header = Frame(root, bg="#FFBB00", bd=5)
header.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)
headerlabel = Label(header, text="DELETE BOOKS", bg="black", fg="white", font=("Courier", 35, "bold"))
headerlabel.place(relx=0, rely=0, relwidth=1, relheight=1)

labelFrame = Frame(root, bg='black')
labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
lb2 = Label(labelFrame, text="Student ID  ", bg='black', fg='white', font=("Helvetica bold", 15))
lb2.place(relx=0.05, rely=0.11)

bookId = Entry(labelFrame)
bookId.place(relx=0.2, rely=0.10, relwidth=0.39, relheight=0.10)

Label(labelFrame, text="%-20s%-25s" % (
        'Book ID', 'Name'),
          bg="black", fg="white", font=("Helvetica bold", 12)).place(relx=0.06, rely=0.3)

def viewBooks():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="Student")
    cursor = conn.cursor()

    bid = bookId.get()

    books = "select Id, Name from StudentInfo where Id='" + bid + "'"
    cursor.execute(books)

    if books is not None:
        for i in cursor:
            Label(labelFrame,
            text="%-15s%-25s" % (i[0], i[1])
                  , bg="black", fg="white", font=("Helvetica bold", 12)).place(relx=0.06, rely=0.45)
            conn.commit()
            cursor.close()
    else:
        pass

def delete():

    conn = mysql.connector.connect(host="localhost", user="root", password="", database="Student")
    cursor = conn.cursor()

    bid = bookId.get()

    deleteSql = "delete from StudentInfo where Id = '" + bid + "'"
    try:
        cursor.execute(deleteSql)
        conn.commit()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except Exception as e:
        print(e)

    root.destroy()

selectBtn = Button(labelFrame, text="Select Book", command=viewBooks)
selectBtn.place(relx=0.8, rely=0.10, relwidth=0.18, relheight=0.09)

# Submit Button
SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=delete, font=("times new roman", 15, "bold"))
SubmitBtn.place(relx=0.28, rely=0.85, relwidth=0.18, relheight=0.08)

quitBtn = Button(root, text="QUIT", bg='#f7f1e3', fg='black', command=root.destroy, font=("times new roman", 15, "bold"))
quitBtn.place(relx=0.53, rely=0.85, relwidth=0.18, relheight=0.08)

root.mainloop()

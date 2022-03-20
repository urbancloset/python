import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import mysql
from PIL import ImageTk, Image
import webbrowser
from tkinter import filedialog



root = tk.Tk()
root.title("View Books")
root.attributes("-fullscreen", True)
root.geometry("2000x1500")

header = Frame(root, bg="#FFBB00", bd=5)
header.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)
headerlabel = Label(header, text="VIEW STUDENT DATA", bg="black", fg="white", font=("Courier", 35, "bold"))
headerlabel.place(relx=0, rely=0, relwidth=1, relheight=1)
labelFrame = Frame(root, bg="black")
labelFrame.place(relx=0.03, rely=0.3, relwidth=0.95, relheight=0.55)
y = 0.20
x = 0.04
canvas = Canvas(labelFrame)
Label(labelFrame, text="%-20s%-25s%-35s" % (
'Name', 'RollNo', 'Standard'),
bg="black", fg="white", font=("Helvetica bold", 12)).place(relx=0.04, rely=0.1)
scrollbar = Scrollbar(labelFrame, orient="vertical", command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
scrollable_frame = Frame(canvas)
canvas.configure(yscrollcommand=scrollbar.set)
scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="Student")
    cursor = conn.cursor()
    viewBooks = "select * from StudentInfo"
    cursor.execute(viewBooks)
    result = cursor.fetchall()
    conn.commit()
    xy = []
    for i in result:
        xy.append(
            Label(labelFrame,
                      text="%-15s%-25s%-20s" % (i[0], i[1], i[2])
                      , bg="black", fg="white", font=("Helvetica bold", 12), anchor=N)
            )
        print(i)
    print(xy)
    for i in xy:
        y = y + 0.1
        i.place(relx=x, rely=y)
    cursor.close()
except Exception as e:
    print(e)

quitBtn = Button(labelFrame, text="QUIT", bg='#f7f1e3', fg='black', font=("times new roman", 15, "bold")
                     , command=root.destroy)
quitBtn.place(relx=0.43, rely=0.9, relwidth=0.18, relheight=0.08)

root.mainloop()

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import mysql
from PIL import ImageTk, Image
import webbrowser
from tkinter import filedialog


root = tk.Tk()
root.title("Add Student Info")
root.attributes("-fullscreen", True)
root.geometry("2000x1500")
header = Frame(root, bg="#000000", bd=5)
header.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)
headerlabel = Label(header, text="ADD STUDENT DATA", bg="white", fg="black", font=("Courier", 35, "bold"))
headerlabel.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = Frame(root, bg="black")
frame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)
Label(frame, text="Name  ", font=("Helvetica bold", 25), bg="black", fg="white").place(relx=0.03, rely=0.2
                                                                                                , relheight=0.08)
StudentName = Entry(frame)
StudentName.place(relx=0.2, rely=0.2, relwidth=0.50, relheight=0.08)

Label(frame, text="RollNo  ", font=("Helvetica bold", 25), bg="black", fg="white").place(relx=0.03, rely=0.3
                                                                                                  , relheight=0.08)
RollNo = Entry(frame)
RollNo.place(relx=0.2, rely=0.3, relwidth=0.50, relheight=0.08)
Label(frame, text="Standard  ", font=("Helvetica bold", 25), bg="black", fg="white").place(relx=0.03, rely=0.4
                                                                                                  , relheight=0.08)
Standard = Entry(frame)
Standard.place(relx=0.2, rely=0.4, relwidth=0.50, relheight=0.08)


#filename = ""

#def UploadAction():
    #nonlocal filename
    #filename = filedialog.askopenfilename(filetypes=[('*jpeg', '*png')])
    #print("Selected", filename)
    #Label(frame, text=filename, font=("Helvetica bold", 10), bg="black", fg="white").place(relx=0.3, rely=0.8
     #                                                                                          , relheight=0.08)
    #Label(frame, text="Photo  ", font=("Helvetica bold", 25), bg="black", fg="white").place(relx=0.03, rely=0.8
     #                                                                                       , relheight=0.08)
    #StudentPhoto = Button(frame, text="Upload Image", command=UploadAction)
    #StudentPhoto.place(relx=0.2, rely=0.8, relheight=0.08)

def StudentRegister():
    #nonlocal filename

    Name = StudentName.get()
    roll = RollNo.get()
    std = Standard.get()
    #Photo = filename
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="Student")
        cursor = conn.cursor()
        insertStudents = "insert into StudentInfo(Name,Rollno,Standard) values ('" + Name + "','" + roll + "','" + std + "') "
        cursor.execute(insertStudents)
        conn.commit()
        messagebox.showinfo('Success', "Student added successfully")
        conn.close()
    except Exception as e:
        print(e)

SubmitBtn = Button(frame, text="SUBMIT", bg='#d1ccc0', font=("times new roman", 15, "bold"), fg='black'
                       , command=StudentRegister)
SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

quitBtn = Button(frame, text="QUIT", bg='#f7f1e3', fg='black', font=("times new roman", 15, "bold")
                     , command=root.destroy)
quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

root.mainloop()

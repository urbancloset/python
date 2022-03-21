from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector as mysql

def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id=="" or name=="" or phone==""):
        messagebox.showinfo("Insert Status","All Fields are required !!")
    else:
        con = mysql.connect(host="localhost",user="root",password="",database="test")
        cursor = con.cursor()
        cursor.execute("insert into employee values('"+id+"','"+name+"','"+phone+"')")
        cursor.execute("commit")

        #clearing textboxes
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')

        show()
        messagebox.showinfo("insert status","inserted successfully !!")

def update():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id=="" or name=="" or phone==""):
        messagebox.showinfo("update Status","All Fields are required !!")
    else:
        con = mysql.connect(host="localhost",user="root",password="",database="test")
        cursor = con.cursor()
        cursor.execute("update employee set name = '"+name+"', phone = '"+phone+"' where id = '"+id+"'")
        cursor.execute("commit")

        #clearing textboxes
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')

        show()
        messagebox.showinfo("update status","updated successfully !!")

def delete():
    id = e_id.get()
   
    if(id==""):
        messagebox.showinfo("delete Status","id is required !!")
    else:
        con = mysql.connect(host="localhost",user="root",password="",database="test")
        cursor = con.cursor()
        cursor.execute("delete from employee where id = '"+id+"'")
        cursor.execute("commit")

        #clearing textboxes
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')

        show()
        messagebox.showinfo("delete status","delete successfully !!")

def show():
    list.delete(0,'end')
    con = mysql.connect(host="localhost",user="root",password="",database="test")
    cursor = con.cursor()
    cursor.execute("Select * from employee")
    rows = cursor.fetchall()

    for row in rows:
        displayRow = str(row[0])+'         '+ row[1]
        list.insert(list.size()+1,displayRow)
    
    con.close()

frame = Tk()
frame.geometry("600x300")

frame.title("Sql Connectivity")

id = Label(frame,text='Enter id',font=('bold',10))
id.place(x=20,y=30)

name = Label(frame,text='Enter Name',font=('bold',10))
name.place(x=20,y=60)

phone = Label(frame,text='Enter Phone no',font=('bold',10))
phone.place(x=20,y=90)

list = Listbox(frame)
list.place(x=310,y=30)

e_id = Entry()
e_id.place(x=150,y=30)

e_name = Entry()
e_name.place(x=150,y=60)

e_phone = Entry()
e_phone.place(x=150,y=90)

insertBtn = Button(frame,text="insert",font=('italic',10),bg="white",command=insert)
insertBtn.place(x=20,y=140)

deleteBtn = Button(frame,text="delete",font=('italic',10),bg="white",command=delete)
deleteBtn.place(x=70,y=140)

updateBtn = Button(frame,text="update",font=('italic',10),bg="white",command=update)
updateBtn.place(x=130,y=140)

showBtn = Button(frame,text="show",font=('italic',10),bg="white",command=show)
showBtn.place(x=190,y=140)

frame.mainloop()

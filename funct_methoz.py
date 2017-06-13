#importing libraries.
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
from tkinter import*

#importing index to access some data
from index import*

#database connection & create a table to store data
def Databaseconnect():
    global conn, cursor
    conn = sqlite3.connect('pythontodo.db')
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `todolist` (task_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, todovalue TEXT)")

#method to create a task and insrt into database
def Create():
    if TODO.get() == "":
        txt_output.config(text="Sorry the field is empty!", fg="red")
    else:
        Databaseconnect()
        cursor.execute("INSERT INTO `todolist` (todovalue) VALUES(?)", (str(TODO.get()),))
        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `todolist` ORDER BY `todovalue` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0]))
        conn.commit()
        TODO.set("")
        cursor.close()
        conn.close()
        txt_output.config(text="Created a data!", fg="blue")

#delete function:
def Delete():
    if not tree.selection():
        txt_output.config(text="Please select a task you would like to delete", fg="red")
    else:
        result = tkMessageBox.askquestion('TODOList APPLICATION', 'Are you sure you want to delete this task?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Databaseconnect()
            cursor.execute("DELETE FROM `todolist` WHERE `task_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
            txt_output.config(text="Task has been deleted", fg="black")

#read values function
def Read():
    tree.delete(*tree.get_children())
    Databaseconnect()
    cursor.execute("SELECT * FROM `todolist` ORDER BY `todovalue` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0]))
    cursor.close()
    conn.close()
    txt_output.config(text="Data has been read", fg="blue")

#update the task:
def Update():
    Databaseconnect()
    if TODO.get() == "":
        txt_output.config(text="Please select a task you would like to update", fg="red")
    else:
        tree.delete(*tree.get_children())
        cursor.execute("UPDATE `todolist` SET `firstname` = ? WHERE `todovalue` = ?",
                       (str(TODO.get()), StringVar(todovalue)))
        conn.commit()
        cursor.execute("SELECT * FROM `todolist` ORDER BY `todovalue` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0]))
        cursor.close()
        conn.close()
        TODO.set("")
        evnt_create.config(state=NORMAL)
        evnt_read.config(state=NORMAL)
        evnt_update.config(state=DISABLED)
        evnt_delete.config(state=NORMAL)
        txt_output.config(text="Task has been successifully edited", fg="blue")

#when u select event to update:
def OnSelected(event):
    global task_id;
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    task_id = selecteditem[0]
    TODO.set("")
    TODO.set(selecteditem[1])
    btn_create.config(state=DISABLED)
    btn_read.config(state=DISABLED)
    btn_update.config(state=NORMAL)
    btn_delete.config(state=DISABLED)

#exit function:
def Exit():
    result = tkMessageBox.askquestion('TODOList APPLICATION', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        start_root.destroy()
        exit()

#variable declaration and assign
TODO = StringVar()

#windows form size
Up = Frame(start_root, width=300, height=50, bd=8, relief="raise")
Up.pack(side=TOP)
Left = Frame(start_root, width=300, height=200, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(start_root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)

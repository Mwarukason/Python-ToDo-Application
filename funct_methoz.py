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

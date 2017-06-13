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

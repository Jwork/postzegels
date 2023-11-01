import sqlite3
from sqlite3 import Error

import tkinter as tk
import tkinter.ttk as ttk

import ui


def create_connection(db_file:str)->sqlite3.Connection | None:
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def exec_sql(conn:sqlite3.Connection, sql:str)->None:
    try:
        c = conn.cursor()
        c.execute(sql)
        print ("SQL executed succesfully")
        # conn.commit()
        # print(c.lastrowid)
    except Error as e:
        print("SQL Error has occured: ") 
        print(e)
    
    rows = c.fetchall()
    print(len(rows))
    if len(rows) == 0:
        print("zero rows returned")
    else:
        for row in rows:
            print(row)

# str_sql = """ CREATE TABLE IF NOT EXISTS landen(
#                 id INTEGER PRIMARY KEY,
#                 land text NOT NULLcle
#                 );"""




str_sql =  """SELECT * FROM landen"""

if __name__ == '__main__':
    # exec_sql(create_connection("db\\postzegels.db"), str_sql)
    ui.setupUI()

print("Thank you for using our application")


#  Write a program to connect to a database and create a table.

import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

# Create table
cursor.execute("""
               CREATE TABLE IF NOT EXISTS students (
                   id INTEGER PRIMARY KEY ,
                   name TEXT NOT NULL,
                   age INTEGER,
                   course TEXT  
               )
               """)
print('Table is created successfully !')

conn.commit()
conn.close()
# Write a program to perform INSERT, UPDATE, DELETE,and SELECT operations on a database.

import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   age INTEGER,
                   course TEXT
               )
               """)

print('Table is created successefully')

# ******************Insert Operation**************************
cursor.execute("INSERT INTO students(name , age , course) VALUES(? ,? ,?)", ("Aditya Vishwakarma",20 ,"BCA"))
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",("Rahul", 21, "MCA"))
cursor.execute('INSERT INTO students(name , age , course) VALUES(? ,? ,?)', ("Mohit sahu",20 ,"BCA"))
cursor.execute('INSERT INTO students(name , age , course) VALUES(? ,? ,?)', ("Sujeet verma",20 ,"BCA"))

print("Data inserted successfully")

# ***************************SELECT OPERATION******************************
print("All records")
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(row)

# ****************************UPADTE OPERATION*********************
cursor.execute('UPDATE students SET age = ? WHERE name = ?',(25 , 'Aditya Vishwakarma'))
cursor.execute('UPDATE students SET course = ? WHERE name = ?',('MCA' , 'Mohit sahu'))
print("\n Data update successefully !")
print("")
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()
for row in rows:
    print(row)
    
# ***************************DELETE OPERATION********************
cursor.execute('DELETE FROM students WHERE name =?',("Mohit sahu",))
print("")
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()
for row in rows:
    print(row)
    
conn.commit()
conn.close()
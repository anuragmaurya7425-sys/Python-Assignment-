#  Demonstrate transaction control (commit and rollback) in database operations.

import sqlite3
conn = sqlite3.connect("Admin.db")
cursor = conn.cursor()

# create table
cursor.execute("""
                CREATE TABLE IF NOT EXISTS student (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    balance INTEGER
                )
                """)

# INSERT VALUE
cursor.execute("INSERT INTO student (name , balance) VALUES (? , ?)",("Aditya",75000))
cursor.execute('INSERT INTO student (name , balance) VALUES (? , ?)',("Mohit",50000))
cursor.execute('INSERT INTO student (name , balance) VALUES (? , ?)',("Sujeet",60000))
print("\n Value Inserted successfully!")

conn.commit()

try:
    print("\n Transaction started! ")
    cursor.execute('UPDATE student SET balance = balance - 5000 WHERE name = ?' ,('Aditya',))
    cursor.execute('UPDATE student SET balance = balance + 10000 WHERE name =?',('Mohit',))
    
    conn.commit()
    print("Transaction committed successfully !")

except Exception as e:
    print("Error occurs :",e)
    conn.rollback()
    print("Transaction rollback !")

        
print("\n Final Record ")
cursor.execute('SELECT * FROM student')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
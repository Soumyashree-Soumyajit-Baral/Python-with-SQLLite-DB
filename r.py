import sqlite3

conn= sqlite3.connect("address.db")
cursor=conn.cursor()

cursor.execute("SELECT * FROM address")
print(cursor.fetchall())
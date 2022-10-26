import sqlite3

conn= sqlite3.connect("address.db")
cursor=conn.cursor()

cursor.execute("UPDATE address SET pin=759001")
conn.commit()
conn.close()
import sqlite3

conn= sqlite3.connect("address.db")
cursor=conn.cursor()

cursor.execute("DELETE FROM address WHERE name='mamba'")
conn.commit()
conn.close()
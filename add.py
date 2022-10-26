import sqlite3

conn= sqlite3.connect("address.db")
cursor=conn.cursor()

cursor.execute("INSERT INTO address VALUES ('SOUMYA', 'Dhenkanal', 'Dhenkanal', 759001, 'Odisha')")
cursor.execute("INSERT INTO address VALUES ('SOUMYAJIT', 'Dhenkanal', 'Dhenkanal', 759025, 'Odisha')")
cursor.execute("INSERT INTO address VALUES ('mamba', 'Dhenkanal', 'Dhenkanal', 759025, 'Odisha')")

conn.commit()
conn.close()
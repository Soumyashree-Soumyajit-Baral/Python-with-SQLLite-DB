import sqlite3

conn= sqlite3.connect("address.db")
cursor=conn.cursor()

table= "CREATE TABLE IF NOT EXISTS address(name TEXT, city TEXT, district TEXT, pin INTEGER, state TEXT)"
cursor.execute(table)

import sqlite3 as SQL

Connection = SQL.connect("Password-locker/Github/Passowrd-locker/Password Locker.db")

cursor = Connection.cursor()

cursor.execute("SQL CODE HERE")

Connection.commit() #Sends code to database


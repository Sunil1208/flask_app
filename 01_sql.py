# import the sqlite library
import os
import sqlite3
from sqlite3.dbapi2 import Cursor

PATH = "/home/sunil/SQLITE3"
db_path = os.path.join(PATH, "my_db.db")

# create a new database if the database doesn't already exist
conn = sqlite3.connect(db_path)

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table

cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
                """)

# close the database connection
conn.close()
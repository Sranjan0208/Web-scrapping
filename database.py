from multiprocessing import connection
import sqlite3
import csv
from datetime import date

# Connect to database
connection = sqlite3.connect('scrapper.db')

# Create cursor
cursor = connection.cursor()

article = """CREATE TABLE IF NOT EXISTS Articles (
    id_number INTEGER PRIMARY KEY AUTOINCREMENT,
    headline TEXT,
    url TEXT,
    author TEXT,
    published REAL
    );"""

cursor.execute(article)
# open a csv file

# with open('2022-08-31_theVerge.csv', 'r') as file:
#     no_records = 0
#     for row in file:
#         cursor.execute(
#             "INSERT INTO Articles VALUES(?, ?, ? , ?, ?)", row.split(','))
#         conn.commit()
#         no_records += 1
# conn.close()
# print("\n{} records inserted.".format(no_records))

# # print("\nDatabase created.")
# # conn.close()

# Opening the person-records.csv file
file = open(f"{date.today()}_theVerge.csv")

# Reading the contents of the
# person-records.csv file
contents = csv.reader(file)

# SQL query to insert data into the
# person table
insert_records = "INSERT INTO Articles (headline, url, author, published) VALUES(?, ?, ?, ?)"

# Importing the contents of the file
# into our person table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM Articles"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)

# Committing the changes
connection.commit()

# closing the database connection
connection.close()

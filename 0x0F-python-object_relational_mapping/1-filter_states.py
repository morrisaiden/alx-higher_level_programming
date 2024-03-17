#!/usr/bin/python3


import MySQLdb
from sys import argv

"""
This Python script connects to a MySQL database and retrieves all rows
from the states table where the state names start with the letter 'N'
"""
if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%'ORDER BY id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)

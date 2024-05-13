import re

import mysql.connector
import json

from server.database.validation import Validation

# connect DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="sellcar"
)

validation = Validation(mydb)

class DatabaseValidation:
    def validate_db(self):
        validation.check_table_exists()

class Database:
    def __init__(self,database_name):
        self.database_name = database_name

    def read(self):
        mycursor = mydb.cursor(dictionary=True)
        sql = f"SELECT * FROM {self.database_name}"

        mycursor.execute(sql)
        # Fetch all the results
        results = mycursor.fetchall()
        return results

    def get_by_id(self,id):
        mycursor = mydb.cursor(dictionary=True)
        sql = f"SELECT * FROM {self.database_name} WHERE id = {id}"

        mycursor.execute(sql)
        # Fetch all the results
        results = mycursor.fetchone()
        return results
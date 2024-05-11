import re

import mysql.connector
import json

from validation import Validation

# connect DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="sellcar"
)

validation = Validation(mydb)
validation.check_table_exists()
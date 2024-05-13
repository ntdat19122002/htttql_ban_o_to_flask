import re

import mysql.connector
import json

from server.database.validation import ValidationDw
from server.database.db import Database

# connect DB
mydb_dw = mysql.connector.connect(
    host="localhost",
    user="root",
    database="sellcar_dw"
)

validation = ValidationDw(mydb_dw)
validation.check_table_exists()

hoa_don = Database('hoa_don')

class Etl:
    def etl(self):
        for hoa_don_record in hoa_don:
            
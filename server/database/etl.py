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
mycursor = mydb_dw.cursor()

validation = ValidationDw(mydb_dw)
validation.check_table_exists()

hoa_don = Database('hoa_don')
o_to = Database('o_to')

class Etl:
    def etl(self):
        for hoa_don_record in hoa_don.read():
            print(o_to.get_by_id(hoa_don_record['o_to_id']))

            mycursor.execute("""
                        INSERT INTO xe (dong,phien_ban,ten,nhien_lieu,so_banh) 
                        VALUES (%s, %s, %s, %s, %s)
                    """, ())

etl = Etl()
etl.etl()
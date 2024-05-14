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
loai_xe = Database('loai_xe')

class Etl:
    def etl(self):
        for hoa_don_record in hoa_don.read():
            o_to_in_hoa_don = o_to.get_by_id(hoa_don_record['o_to_id'])
            loai_xe_info = loai_xe.get_by_id(o_to_in_hoa_don['loai_xe_id'])
            # mycursor.execute("""
            #     INSERT INTO xe (dong,phien_ban,ten,nhien_lieu,so_banh)
            #     VALUES (%s, %s, %s, %s, %s)
            # """,
            # (loai_xe_info['dong'],loai_xe_info['phien_ban'],loai_xe_info['ten'],loai_xe_info['nhien_lieu'],loai_xe_info['so_banh']))

            # quy = 1
            # thang = hoa_don_record['thoi_gian'].month
            # if thang >= 4  and thang <= 6:
            #     quy = 2
            # elif thang >= 7  and thang <= 9:
            #     quy = 3
            # elif thang > 9:
            #     quy = 4
            #
            # mycursor.execute("""
            #     INSERT INTO thoi_gian (thang,quy,nam)
            #     VALUES (%s, %s, %s)
            # """,
            # (thang,quy,hoa_don_record['thoi_gian'].year))

            mydb_dw.commit()
etl = Etl()
etl.etl()
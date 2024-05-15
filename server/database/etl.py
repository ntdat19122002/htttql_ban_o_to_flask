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
mycursor = mydb_dw.cursor(dictionary=True)

validation = ValidationDw(mydb_dw)
validation.check_table_exists()

hoa_don = Database('hoa_don')
o_to = Database('o_to')
loai_xe = Database('loai_xe')
nhan_vien = Database('nhan_vien')
chi_nhanh = Database('chi_nhanh')
nguoi_dung = Database('nguoi_dung')

class Etl:
    def etl(self):
        for hoa_don_record in hoa_don.read():
            o_to_in_hoa_don = o_to.get_by_id(hoa_don_record['o_to_id'])
            loai_xe_info = loai_xe.get_by_id(o_to_in_hoa_don['loai_xe_id'])
            nhan_vien_info = nhan_vien.get_by_id(hoa_don_record['nhan_vien_id'])
            chi_nhanh_nhan_vien = chi_nhanh.get_by_id(nhan_vien_info['chi_nhanh_id'])
            khach_hang_info = nguoi_dung.get_by_id(hoa_don_record['nguoi_dung_id'])

            mycursor.execute("""
                INSERT INTO xe (dong,phien_ban,ten,nhien_lieu,so_banh)
                VALUES (%s, %s, %s, %s, %s)
            """,
            (loai_xe_info['dong'],loai_xe_info['phien_ban'],loai_xe_info['ten'],loai_xe_info['nhien_lieu'],loai_xe_info['so_banh']))
            xe_id = mycursor.lastrowid

            quy = 1
            thang = hoa_don_record['thoi_gian'].month
            if thang >= 4  and thang <= 6:
                quy = 2
            elif thang >= 7  and thang <= 9:
                quy = 3
            elif thang > 9:
                quy = 4
            nam = hoa_don_record['thoi_gian'].year

            mycursor.execute("""
                SELECT *
                FROM thoi_gian
                WHERE thang = %s AND quy = %s AND nam = %s
            """, (thang, quy, nam))
            result = mycursor.fetchone()
            if result:
                thoi_gian_id = result['id']
            else:
                mycursor.execute("""
                    INSERT INTO thoi_gian (thang, quy, nam)
                    VALUES (%s, %s, %s)
                """,
                (thang,quy,nam))
                thoi_gian_id = mycursor.lastrowid

            mycursor.execute("""
                             SELECT * FROM xuat_su WHERE quoc_gia = %s AND hang = %s
                        """, (loai_xe_info['xuat_su'],loai_xe_info['hang']))
            result = mycursor.fetchone()
            if result:
                xuat_su_id = result['id']
            else:
                mycursor.execute("""
                    INSERT INTO xuat_su (quoc_gia,hang)
                    VALUES (%s, %s)
                """,
                (loai_xe_info['xuat_su'],loai_xe_info['hang']))
                xuat_su_id = mycursor.lastrowid

            mycursor.execute("""
                SELECT *
                FROM ban_hang
                WHERE chi_nhanh = %s AND ten_nguoi_ban = %s AND email_nguoi_ban = %s AND chuc_vu = %s
            """, (chi_nhanh_nhan_vien['ten'],nhan_vien_info['ten'],nhan_vien_info['email'],nhan_vien_info['chuc_vu']))
            result = mycursor.fetchone()
            if result:
                ban_hang_id = result['id']
            else:
                mycursor.execute("""
                    INSERT INTO ban_hang (chi_nhanh,ten_nguoi_ban,email_nguoi_ban,chuc_vu)
                    VALUES (%s, %s, %s, %s)
                """,
                    (chi_nhanh_nhan_vien['ten'],nhan_vien_info['ten'],nhan_vien_info['email'],nhan_vien_info['chuc_vu'])
                )
                ban_hang_id = mycursor.lastrowid

            mycursor.execute("""
                SELECT *
                FROM khach_hang
                WHERE dia_chi = %s AND email = %s AND sdt = %s
            """, (khach_hang_info['dia_chi'],khach_hang_info['email'],khach_hang_info['so_dien_thoai']))
            result = mycursor.fetchone()
            if result:
                khach_hang_id = result['id']
            else:
                mycursor.execute("""
                        INSERT INTO khach_hang (dia_chi, email, sdt)
                        VALUES (%s, %s, %s))
                    """,
                    (khach_hang_info['dia_chi'],khach_hang_info['email'],khach_hang_info['so_dien_thoai'])
                )
                khach_hang_id = mycursor.lastrowid

            mycursor.execute("""
                INSERT INTO fact_sale (khach_hang_id,ban_hang_id,xe_id,thoi_gian_id,xuat_su_id,gia_nhap,gia_ban)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
                 (khach_hang_id, ban_hang_id, xe_id,
                  thoi_gian_id,xuat_su_id,o_to_in_hoa_don['gia_nhap'],o_to_in_hoa_don['gia_ban']))

            mydb_dw.commit()
etl = Etl()
etl.etl()
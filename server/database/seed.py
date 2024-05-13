import re
import random

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
mycursor = mydb.cursor()

class Seed:
    def fake_loai_xe(self):
        sql = """
            INSERT INTO loai_xe (hang, ten, dong, phien_ban, nhien_lieu, mo_ta, hinh_anh, xuat_su, so_banh) VALUES
            ('Toyota', 'Corolla', 'XE2024', 'Standard', 'Xăng', 'Mô tả xe Corolla', 'corolla.jpg', 'Nhật Bản', 4),
            ('Toyota', 'Camry', 'XE2024', 'Deluxe', 'Xăng', 'Mô tả xe Camry', 'camry.jpg', 'Nhật Bản', 4),
            ('Toyota', 'Rav4', 'XE2024', 'Standard', 'Xăng', 'Mô tả xe Rav4', 'rav4.jpg', 'Nhật Bản', 4),
            ('Toyota', 'Highlander', 'XE2024', 'Premium', 'Dầu', 'Mô tả xe Highlander', 'highlander.jpg', 'Nhật Bản', 4),
            ('Toyota', 'Land Cruiser', 'XE2024', 'Deluxe', 'Dầu', 'Mô tả xe Land Cruiser', 'land_cruiser.jpg', 'Nhật Bản', 4),
            ('Honda', 'Civic', 'XE2024', 'Standard', 'Xăng', 'Mô tả xe Civic', 'civic.jpg', 'Nhật Bản', 4),
            ('Honda', 'Accord', 'XE2024', 'Deluxe', 'Xăng', 'Mô tả xe Accord', 'accord.jpg', 'Nhật Bản', 4),
            ('Honda', 'CR-V', 'XE2024', 'Standard', 'Dầu', 'Mô tả xe CR-V', 'crv.jpg', 'Nhật Bản', 4),
            ('Honda', 'Pilot', 'XE2024', 'Premium', 'Dầu', 'Mô tả xe Pilot', 'pilot.jpg', 'Nhật Bản', 4),
            ('Honda', 'Odyssey', 'XE2024', 'Deluxe', 'Dầu', 'Mô tả xe Odyssey', 'odyssey.jpg', 'Nhật Bản', 4),
            ('Ford', 'Focus', 'XE2024', 'Standard', 'Xăng', 'Mô tả xe Focus', 'focus.jpg', 'Mỹ', 4),
            ('Ford', 'Fiesta', 'XE2024', 'Deluxe', 'Xăng', 'Mô tả xe Fiesta', 'fiesta.jpg', 'Mỹ', 4),
            ('Ford', 'Escape', 'XE2024', 'Standard', 'Dầu', 'Mô tả xe Escape', 'escape.jpg', 'Mỹ', 4),
            ('Ford', 'Explorer', 'XE2024', 'Premium', 'Dầu', 'Mô tả xe Explorer', 'explorer.jpg', 'Mỹ', 4),
            ('Ford', 'Expedition', 'XE2024', 'Deluxe', 'Dầu', 'Mô tả xe Expedition', 'expedition.jpg', 'Mỹ', 4),
            ('Hyundai', 'Elantra', 'XE2024', 'Standard', 'Xăng', 'Mô tả xe Elantra', 'elantra.jpg', 'Hàn Quốc', 4),
            ('Hyundai', 'Sonata', 'XE2024', 'Deluxe', 'Xăng', 'Mô tả xe Sonata', 'sonata.jpg', 'Hàn Quốc', 4),
            ('Hyundai', 'Tucson', 'XE2024', 'Standard', 'Dầu', 'Mô tả xe Tucson', 'tucson.jpg', 'Hàn Quốc', 4),
            ('Hyundai', 'Santa Fe', 'XE2024', 'Premium', 'Dầu', 'Mô tả xe Santa Fe', 'santafe.jpg', 'Hàn Quốc', 4),
            ('Hyundai', 'Palisade', 'XE2024', 'Deluxe', 'Dầu', 'Mô tả xe Palisade', 'palisade.jpg', 'Hàn Quốc', 4),
            ('Kia', 'Forte', 'XE2024', 'Standard', 'Xăng', 'Mô tả xe Forte', 'forte.jpg', 'Hàn Quốc', 4),
            ('Kia', 'Optima', 'XE2024', 'Deluxe', 'Xăng', 'Mô tả xe Optima', 'optima.jpg', 'Hàn Quốc', 4),
            ('Kia', 'Sportage', 'XE2024', 'Standard', 'Dầu', 'Mô tả xe Sportage', 'sportage.jpg', 'Hàn Quốc', 4),
            ('Kia', 'Sorento', 'XE2024', 'Premium', 'Dầu', 'Mô tả xe Sorento', 'sorento.jpg', 'Hàn Quốc', 4),
            ('Kia', 'Telluride', 'XE2024', 'Deluxe', 'Dầu', 'Mô tả xe Telluride', 'telluride.jpg', 'Hàn Quốc', 4),
            ('Chevrolet', 'Cruze', 'XE2024', 'Standard', 'Xăng', 'Mô tả xe Cruze', 'cruze.jpg', 'Mỹ', 4),
            ('Chevrolet', 'Malibu', 'XE2024', 'Deluxe', 'Xăng', 'Mô tả xe Malibu', 'malibu.jpg', 'Mỹ', 4),
            ('Chevrolet', 'Equinox', 'XE2024', 'Standard', 'Dầu', 'Mô tả xe Equinox', 'equinox.jpg', 'Mỹ', 4),
            ('Chevrolet', 'Traverse', 'XE2024', 'Premium', 'Dầu', 'Mô tả xe Traverse', 'traverse.jpg', 'Mỹ', 4),
            ('Chevrolet', 'Tahoe', 'XE2024', 'Deluxe', 'Dầu', 'Mô tả xe Tahoe', 'tahoe.jpg', 'Mỹ', 4),
            ('Nissan', 'Sentra', 'XE2024', 'Standard', 'Xăng', 'Mô tả xe Sentra', 'sentra.jpg', 'Nhật Bản', 4),
            ('Nissan', 'Altima', 'XE2024', 'Deluxe', 'Xăng', 'Mô tả xe Altima', 'altima.jpg', 'Nhật Bản', 4),
            ('Nissan', 'Rogue', 'XE2024', 'Standard', 'Dầu', 'Mô tả xe Rogue', 'rogue.jpg', 'Nhật Bản', 4),
            ('Nissan', 'Pathfinder', 'XE2024', 'Premium', 'Dầu', 'Mô tả xe Pathfinder', 'pathfinder.jpg', 'Nhật Bản', 4),
            ('Nissan', 'Armada', 'XE2024', 'Deluxe', 'Dầu', 'Mô tả xe Armada', 'armada.jpg', 'Nhật Bản', 4),
            ('BMW', '3 Series', 'XE2024', 'Standard', 'Xăng', 'Mô tả xe 3 Series', '3series.jpg', 'Đức', 4),
            ('BMW', '5 Series', 'XE2024', 'Deluxe', 'Xăng', 'Mô tả xe 5 Series', '5series.jpg', 'Đức', 4),
            ('BMW', 'X3', 'XE2024', 'Standard', 'Dầu', 'Mô tả xe X3', 'x3.jpg', 'Đức', 4),
            ('BMW', 'X5', 'XE2024', 'Premium', 'Dầu', 'Mô tả xe X5', 'x5.jpg', 'Đức', 4),
            ('BMW', 'X7', 'XE2024', 'Deluxe', 'Dầu', 'Mô tả xe X7', 'x7.jpg', 'Đức', 4),
            ('Mercedes-Benz', 'C-Class', 'XE2024', 'Standard', 'Xăng', 'Mô tả xe C-Class', 'cclass.jpg', 'Đức', 4),
            ('Mercedes-Benz', 'E-Class', 'XE2024', 'Deluxe', 'Xăng', 'Mô tả xe E-Class', 'eclass.jpg', 'Đức', 4),
            ('Mercedes-Benz', 'GLC', 'XE2024', 'Standard', 'Dầu', 'Mô tả xe GLC', 'glc.jpg', 'Đức', 4),
            ('Mercedes-Benz', 'GLE', 'XE2024', 'Premium', 'Dầu', 'Mô tả xe GLE', 'gle.jpg', 'Đức', 4),
            ('Mercedes-Benz', 'GLS', 'XE2024', 'Deluxe', 'Dầu', 'Mô tả xe GLS', 'gls.jpg', 'Đức', 4),
            ('Audi', 'A4', 'XE2024', 'Standard', 'Xăng', 'Mô tả xe A4', 'a4.jpg', 'Đức', 4),
            ('Audi', 'A6', 'XE2024', 'Deluxe', 'Xăng', 'Mô tả xe A6', 'a6.jpg', 'Đức', 4),
            ('Audi', 'Q5', 'XE2024', 'Standard', 'Dầu', 'Mô tả xe Q5', 'q5.jpg', 'Đức', 4),
            ('Audi', 'Q7', 'XE2024', 'Premium', 'Dầu', 'Mô tả xe Q7', 'q7.jpg', 'Đức', 4),
            ('Audi', 'Q8', 'XE2024', 'Deluxe', 'Dầu', 'Mô tả xe Q8', 'q8.jpg', 'Đức', 4);   
        """
        mycursor.execute(sql)
        mydb.commit()
        print('insert 50 record into loai_xe table')

    def fake_o_to(self):
        for _ in range(100):
            loai_xe_id = random.randint(1, 50)
            so_khung = "KH" + str(random.randint(1000, 9999))
            so_may = "SM" + str(random.randint(1000, 9999))
            mau = random.choice(["Red", "Blue", "Green", "Yellow", "Black", "White"])
            ngay_san_xuat = "2024-05-11"  # Example date
            gia_nhap = random.uniform(5000, 20000)
            gia_ban = gia_nhap * random.uniform(1.1, 1.5)
            mo_ta = "Sample description"
            tinh_trang = random.choice(["New", "Used"])
            quang_duong_da_di = random.randint(1000, 10000)
            if tinh_trang == 'New':
                quang_duong_da_di = 0
            video = "https://www.example.com/video"

            # Inserting a record into the "o_to" table
            mycursor.execute("""
                INSERT INTO o_to (loai_xe_id, so_khung, so_may, mau, ngay_san_xuat, gia_nhap, gia_ban, mo_ta, tinh_trang, quang_duong_da_di, video) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
            loai_xe_id, so_khung, so_may, mau, ngay_san_xuat, gia_nhap, gia_ban, mo_ta, tinh_trang, quang_duong_da_di,
            video))
        mydb.commit()
seed = Seed()
seed.fake_o_to()
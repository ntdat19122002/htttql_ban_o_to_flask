import re
import random
from datetime import datetime, timedelta

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

    def fake_nhan_vien(self):
        sql = """
                INSERT INTO nhan_vien (ten, ngay_sinh, dia_chi, email, cccd, hinh_anh, chuc_vu, mat_khau) VALUES
                ('Nguyen Van A', '1990-01-15', '123 Pho Hue, Ha Noi', 'nguyenvana@example.com', '012345678901', 'images/nguyenvana.jpg', 'Nhan vien', 'password1'),
                ('Tran Thi B', '1985-05-20', '456 Le Loi, Ho Chi Minh', 'tranthib@example.com', '012345678902', 'images/tranthib.jpg', 'Truong phong', 'password2'),
                ('Le Van C', '1992-03-10', '789 Tran Hung Dao, Da Nang', 'levanc@example.com', '012345678903', 'images/levanc.jpg', 'Nhan vien', 'password3'),
                ('Pham Thi D', '1988-11-25', '321 Ngo Quyen, Hue', 'phamthid@example.com', '012345678904', 'images/phamthid.jpg', 'Nhan vien', 'password4'),
                ('Hoang Van E', '1991-07-18', '654 Dien Bien Phu, Can Tho', 'hoangvane@example.com', '012345678905', 'images/hoangvane.jpg', 'Nhan vien', 'password5'),
                ('Vu Thi F', '1987-09-09', '987 Ly Thuong Kiet, Hai Phong', 'vuthif@example.com', '012345678906', 'images/vuthif.jpg', 'Nhan vien', 'password6'),
                ('Nguyen Van G', '1983-12-30', '123 Ba Trieu, Nha Trang', 'nguyenvang@example.com', '012345678907', 'images/nguyenvang.jpg', 'Nhan vien', 'password7'),
                ('Tran Thi H', '1995-06-15', '456 Nguyen Trai, Vung Tau', 'tranthih@example.com', '012345678908', 'images/tranthih.jpg', 'Nhan vien', 'password8'),
                ('Le Van I', '1993-08-22', '789 Cach Mang Thang Tam, Da Lat', 'levani@example.com', '012345678909', 'images/levani.jpg', 'Nhan vien', 'password9'),
                ('Pham Thi J', '1990-04-14', '321 Le Duan, Quy Nhon', 'phamthij@example.com', '012345678910', 'images/phamthij.jpg', 'Nhan vien', 'password10'),
                ('Hoang Van K', '1982-11-11', '654 Tran Phu, Phan Thiet', 'hoangvank@example.com', '012345678911', 'images/hoangvank.jpg', 'Nhan vien', 'password11'),
                ('Vu Thi L', '1989-02-28', '987 Hai Ba Trung, Bien Hoa', 'vuthil@example.com', '012345678912', 'images/vuthil.jpg', 'Nhan vien', 'password12'),
                ('Nguyen Van M', '1996-05-05', '123 Tran Quoc Toan, Buon Ma Thuot', 'nguyenvanm@example.com', '012345678913', 'images/nguyenvanm.jpg', 'Nhan vien', 'password13'),
                ('Tran Thi N', '1994-10-23', '456 Hoang Hoa Tham, Rach Gia', 'tranthin@example.com', '012345678914', 'images/tranthin.jpg', 'Nhan vien', 'password14'),
                ('Le Van O', '1991-01-19', '789 Le Hong Phong, Soc Trang', 'levano@example.com', '012345678915', 'images/levano.jpg', 'Nhan vien', 'password15'),
                ('Pham Thi P', '1986-07-30', '321 Tran Quang Khai, My Tho', 'phamthip@example.com', '012345678916', 'images/phamthip.jpg', 'Nhan vien', 'password16'),
                ('Hoang Van Q', '1984-09-18', '654 Nguyen Van Linh, Vinh', 'hoangvanq@example.com', '012345678917', 'images/hoangvanq.jpg', 'Nhan vien', 'password17'),
                ('Vu Thi R', '1993-03-03', '987 Vo Thi Sau, Dong Hoi', 'vuthir@example.com', '012345678918', 'images/vuthir.jpg', 'Nhan vien', 'password18'),
                ('Nguyen Van S', '1990-06-12', '123 Phan Chau Trinh, Tam Ky', 'nguyenvans@example.com', '012345678919', 'images/nguyenvans.jpg', 'Nhan vien', 'password19'),
                ('Tran Thi T', '1988-12-27', '456 Ly Thuong Kiet, Thanh Hoa', 'tranthit@example.com', '012345678920', 'images/tranthit.jpg', 'Nhan vien', 'password20');
                """
        mycursor.execute(sql)
        mydb.commit()
        print('insert 20 record into nhan_vien table')

    def random_date(self,start, end):
        """Generate a random datetime between `start` and `end`"""
        return start + timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())),
        )

    def fake_hoa_don(self):
        used_o_to_ids = set()
        while len(used_o_to_ids) < 50:
            used_o_to_ids.add(random.randint(1, 100))

        start_date = datetime(2013, 1, 1)
        end_date = datetime(2014, 5, 1)

        # Insert 50 fake records
        for i, o_to_id in enumerate(used_o_to_ids, start=1):
            nhan_vien_id = random.randint(1, 20)
            ma_so_thue = f'MST-{i:03d}'
            hinh_thuc_thanh_toan = 'Cash' if i % 2 == 0 else 'Credit Card'
            thoi_gian = self.random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')

            add_hoa_don = (
                "INSERT INTO hoa_don (nhan_vien_id, o_to_id, ma_so_thue, hinh_thuc_thanh_toan, thoi_gian) "
                "VALUES (%s, %s, %s, %s, %s)"
            )
            data_hoa_don = (nhan_vien_id, o_to_id, ma_so_thue, hinh_thuc_thanh_toan, thoi_gian)

            mycursor.execute(add_hoa_don, data_hoa_don)

        # Commit the transaction
        mydb.commit()

seed = Seed()
# seed.fake_loai_xe()
# seed.fake_o_to()
# seed.fake_nhan_vien()
# seed.fake_hoa_don()
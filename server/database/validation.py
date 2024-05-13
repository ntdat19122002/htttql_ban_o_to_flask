class Validation:
    def __init__(self, mydb):
        self.mydb = mydb
        self.mycursor = mydb.cursor()
    def check_table_exists(self):
        table_list = ['loai_xe','tin_tuc','o_to','nguoi_dung','dai_ly','khuyen_mai'
                      ,'nguoi_dung','bai_dang','kho','hoa_don','nhan_vien','bao_hiem']
        for table in table_list:
            if not self.table_exists(self.mycursor, table):
                self.create_table(self.mycursor, table)

    def table_exists(self, cursor, table_name):
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        return cursor.fetchone() is not None

    def create_table(self, cursor, table_name):
        if table_name == 'loai_xe':
            cursor.execute("""
                CREATE TABLE loai_xe (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    hang VARCHAR(255),
                    ten VARCHAR(255),
                    dong VARCHAR(255),
                    phien_ban VARCHAR(255),
                    nhien_lieu VARCHAR(255),
                    mo_ta VARCHAR(255),
                    hinh_anh VARCHAR(255),
                    xuat_su VARCHAR(255),
                    so_banh INT
                )
            """)
        elif table_name == 'kho':
            cursor.execute("""
                CREATE TABLE kho (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    dia_chi VARCHAR(255)
                )
            """)
        elif table_name == 'o_to':
            cursor.execute("""
                CREATE TABLE o_to (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    loai_xe_id INT,
                    FOREIGN KEY (loai_xe_id) REFERENCES loai_xe(id),
                    so_khung VARCHAR(255),
                    so_may VARCHAR(255),
                    mau VARCHAR(255),
                    ngay_san_xuat VARCHAR(255),
                    gia_nhap FLOAT,
                    gia_ban FLOAT,
                    mo_ta VARCHAR(255),
                    tinh_trang VARCHAR(10),
                    quang_duong_da_di INT,
                    video VARCHAR(255)
                )
            """)
        elif table_name == 'nguoi_dung':
            cursor.execute("""
                CREATE TABLE nguoi_dung (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    ten VARCHAR(255),
                    dia_chi VARCHAR(255),
                    so_dien_thoai VARCHAR(255),
                    mat_khau VARCHAR(255)
                )
            """)
        elif table_name == 'bai_dang':
            cursor.execute("""
                CREATE TABLE bai_dang (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    ten VARCHAR(255),
                    noi_dung TEXT,
                    ngay_dang VARCHAR(255)
                )
            """)
        elif table_name == 'khuyen_mai':
            cursor.execute("""
                CREATE TABLE khuyen_mai (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    gia_tri FLOAT,
                    ngay_bat_dau VARCHAR(255),
                    ngay_ket_thuc VARCHAR(255)
                )
            """)
        elif table_name == 'dai_ly':
            cursor.execute("""
                CREATE TABLE dai_ly (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    ten VARCHAR(255),
                    dia_chi VARCHAR(255)
                )
            """)
        elif table_name == 'hoa_don':
            cursor.execute("""
                CREATE TABLE hoa_don (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    content TEXT
                )
            """)
        elif table_name == 'nhan_vien':
            cursor.execute("""
                    CREATE TABLE nhan_vien (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        ten VARCHAR(255),
                        ngay_sinh VARCHAR(255),
                        dia_chi VARCHAR(255),
                        email VARCHAR(255),
                        cccd VARCHAR(255),
                        hinh_anh VARCHAR(255),
                        chuc_vu VARCHAR(255),
                        mat_khau VARCHAR(255)
                    )
                """)
        elif table_name == 'tin_tuc':
            cursor.execute("""
                    CREATE TABLE tin_tuc (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255),
                        content TEXT
                    )
                """)
        elif table_name == 'bao_hiem':
            cursor.execute("""
                    CREATE TABLE bao_hiem (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        ngay_bat_dau VARCHAR(255),
                        ngay_ket_thuc VARCHAR(255),
                        chinh_sach TEXT,
                        gia_tri_min FLOAT,
                        gia_tri_max FLOAT
                    )
                """)

class ValidationDw:
    def __init__(self, mydb):
        self.mydb = mydb
        self.mycursor = mydb.cursor()
    def check_table_exists(self):
        table_list = ['khach_hang','ban_hang','xe','thoi_gian','xuat_su','fact_sale']
        for table in table_list:
            if not self.table_exists(self.mycursor, table):
                self.create_table(self.mycursor, table)

    def table_exists(self, cursor, table_name):
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        return cursor.fetchone() is not None

    def create_table(self, cursor, table_name):
        if table_name == 'khach_hang':
            cursor.execute("""
                CREATE TABLE khach_hang (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    thanh_pho VARCHAR(255),
                    quan VARCHAR(255),
                    email VARCHAR(255),
                    sdt VARCHAR(255)
                )
            """)
        elif table_name == 'ban_hang':
            cursor.execute("""
                CREATE TABLE ban_hang (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    chi_nhanh VARCHAR(255),
                    ten_nguoi_ban VARCHAR(255),
                    email_nguoi_ban VARCHAR(255),
                    chuc_vu VARCHAR(255)
                )
            """)
        elif table_name == 'xe':
            cursor.execute("""
                CREATE TABLE xe (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    dong VARCHAR(255),
                    phien_ban VARCHAR(255),
                    ten VARCHAR(255),
                    nhien_lieu VARCHAR(255),
                    so_banh INT
                )
            """)
        elif table_name == 'thoi_gian':
            cursor.execute("""
                CREATE TABLE thoi_gian (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    tuan INT,
                    thang INT,
                    quy INT,
                    nam INT
                )
            """)
        elif table_name == 'xuat_su':
            cursor.execute("""
                CREATE TABLE xuat_su (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    quoc_gia VARCHAR(255),
                    hang VARCHAR(255)
                )
            """)
        elif table_name == 'fact_sale':
            cursor.execute("""
                CREATE TABLE fact_sale (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    khach_hang_id INT,
                    ban_hang_id INT,
                    xe_id INT,
                    thoi_gian_id INT,
                    xuat_su_id INT,
                    gia_nhap FLOAT,
                    gia_ban FLOAT,
                    FOREIGN KEY (khach_hang_id) REFERENCES khach_hang(id),
                    FOREIGN KEY (ban_hang_id) REFERENCES ban_hang(id),
                    FOREIGN KEY (xe_id) REFERENCES xe(id),
                    FOREIGN KEY (thoi_gian_id) REFERENCES thoi_gian(id),
                    FOREIGN KEY (xuat_su_id) REFERENCES xuat_su(id)
                )
            """)
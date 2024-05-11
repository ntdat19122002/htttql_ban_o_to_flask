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
                print(f"Table {table} created successfully.")
            else:
                print(f"Table {table} already exists.")

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
                    name VARCHAR(255),
                    content TEXT
                )
            """)


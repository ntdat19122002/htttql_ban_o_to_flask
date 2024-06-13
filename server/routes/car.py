from flask import Blueprint, request

car_pb = Blueprint('car',__name__)
from server.database.db import Database, mydb
o_to = Database('o_to')
loai_xe = Database('loai_xe')
nguoi_dung = Database('nguoi_dung')
hoa_don = Database('hoa_don')
@car_pb.route("/car/list")
def list_car():
    return loai_xe.read()

@car_pb.route("/car/new", methods=['POST'])
def get_new_car_by_id():
    return loai_xe.get_by_id(request.json.get('loai_xe_id'))
@car_pb.route("/car/create")
def make_car():
    return "<p>acsin</p>"

@car_pb.route("/oto/list")
def list_o_to():
    return o_to.read()

@car_pb.route("/loai_xe/list")
def list_loai_xe():
    return loai_xe.read()

@car_pb.route("/nguoi_dung/list")
def list_nguoi_dung():
    return nguoi_dung.read()

@car_pb.route("/hoa_don/list")
def list_hoa_don():
    mycursor = mydb.cursor(dictionary=True)
    sql = f"""
        SELECT *
        FROM
            hoa_don
        INNER JOIN
            nguoi_dung ON hoa_don.nguoi_dung_id = nguoi_dung.id
        INNER JOIN
            nhan_vien ON hoa_don.nhan_vien_id = nhan_vien.id
        INNER JOIN
            o_to ON hoa_don.o_to_id = o_to.id;
    """

    mycursor.execute(sql)
    # Fetch all the results
    results = mycursor.fetchall()
    print(results)
    return results

@car_pb.route("/hoa_don_temp/list")
def list_hoa_don_temp():
    mycursor = mydb.cursor(dictionary=True)
    sql = f"""
        SELECT *
        FROM
            hoa_don_temp
        INNER JOIN
            nguoi_dung ON hoa_don_temp.nguoi_dung_id = nguoi_dung.id
        INNER JOIN
            nhan_vien ON hoa_don_temp.nhan_vien_id = nhan_vien.id
        INNER JOIN
            o_to ON hoa_don_temp.o_to_id = o_to.id;
    """

    mycursor.execute(sql)
    # Fetch all the results
    results = mycursor.fetchall()
    print(results)
    return results

@car_pb.route("/hoa_don_temp/new")
    def list_hoa_don_temp():
        mycursor = mydb.cursor()
        sql = "INSERT INTO audio (nguoi_dung_id, o_to_id, thoi_gian) VALUES (%s, %s, %s, %s)"
        values = (nguoi_dung_id o_to_id, thoi_gian)

        mycursor.execute(sql, values)

        # Remember to commit the transaction if you want to make the changes permanent
        mydb.commit()

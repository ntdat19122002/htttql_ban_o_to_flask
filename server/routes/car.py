from flask import Blueprint, request

car_pb = Blueprint('car',__name__)
from server.database.db import Database
o_to = Database('o_to')
loai_xe = Database('loai_xe')

@car_pb.route("/car/list")
def list_car():
    return loai_xe.read()

@car_pb.route("/car/new", methods=['POST'])
def get_new_car_by_id():
    return loai_xe.get_by_id(request.json.get('loai_xe_id'))
@car_pb.route("/car/create")
def make_car():
    return "<p>acsin</p>"

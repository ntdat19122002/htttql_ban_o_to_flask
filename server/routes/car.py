from flask import Blueprint

car_pb = Blueprint('car',__name__)

@car_pb.route("/car/create")
def make_car():
    return "<p>acsin</p>"

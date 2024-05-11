from flask import Blueprint

admin_pb = Blueprint('admin',__name__)

@admin_pb.route("/admin")
def fd():
    return "<p>admin</p>"

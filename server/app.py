from server.routes.admin import admin_pb
from server.routes.car import car_pb
from server.database.db import DatabaseValidation

from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(admin_pb)
app.register_blueprint(car_pb)

DatabaseValidation().validate_db()
@app.route("/")
def register():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from server.routes.admin import admin_pb
from server.routes.car import car_pb

app = Flask(__name__)
app.register_blueprint(admin_pb)
app.register_blueprint(car_pb)

@app.route("/")
def register():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)
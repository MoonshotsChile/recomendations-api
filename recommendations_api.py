import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve

from api.benefits import Benefits
from api.missions import Missions
from api.notifications import Notifications
from api.userdata import Userdata

app = Flask(__name__)
CORS(app)


@app.route('/benefits-v2/benefits/', defaults={'_id': ''}, methods=["GET"])
@app.route('/benefits-v2/benefits/<_id>/', methods=["GET"])
def benefits(_id):
    return Benefits.get(request, _id)


@app.route('/benefits-v2/missions/', defaults={'_id': ''}, methods=["GET"])
@app.route('/benefits-v2/missions/<_id>/', methods=["GET"])
def missions(_id):
    return Missions.get(request, _id)


@app.route('/benefits-v2/notifications/', defaults={'_id': ''}, methods=["GET"])
@app.route('/benefits-v2/notifications/<_id>/', methods=["GET"])
def notifications(_id):
    return Notifications.get(request, _id)


@app.route('/benefits-v2/userdata/', defaults={'_id': ''}, methods=["GET"])
@app.route('/benefits-v2/userdata/<_id>/', methods=["GET"])
def userdata(_id):
    return Userdata.get(request, _id)


@app.route('/benefits-v2/userdata/', defaults={'_id': ''}, methods=["PATCH"])
@app.route('/benefits-v2/userdata/<_id>/', methods=["PATCH"])
def userdata_patch(_id):
    return Userdata.patch(request, _id)


@app.route('/benefits-v2/userdata', methods=["POST"])
def userdata_add():
    return Userdata.add(request)


@app.route('/benefits-v2/userdata/', defaults={'_id': ''}, methods=["DELETE"])
@app.route('/benefits-v2/userdata/<_id>/', methods=["DELETE"])
def userdata_delete(_id):
    return Userdata.delete(request, _id)


def is_port_in_use(_port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', _port)) == 0


def run_server(_port):
    serve(app, host='0.0.0.0', port=_port)


if __name__ == '__main__':
    port = 5002
    if os.environ.get("PYTHON_ENV") == "prod":
        if not is_port_in_use(port):
            run_server(port)
        else:
            print(f"port {port} is already in use, see ya ;)")
    else:
        app.run(debug=True, port=port)

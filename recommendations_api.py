import os
from urllib.request import urlopen
from urllib.parse import urlparse

from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
import json

app = Flask(__name__)
CORS(app)

API_URL = "https://api.moonshots.cl/benefits"


@app.route('/benefits-v2/benefits/', defaults={'id': ''}, methods=["GET"])
@app.route('/benefits-v2/benefits/<id>', methods=["GET"])
def benefits(id):
    query = urlparse(request.url).query
    url = f'{API_URL}/benefits/{id}?{query}'
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    return jsonify(data)


@app.route('/benefits-v2/userdata/', defaults={'id': ''}, methods=["GET"])
@app.route('/benefits-v2/userdata/<id>', methods=["GET"])
def userdata(id):
    query = urlparse(request.url).query
    url = f'{API_URL}/userdata/{id}?{query}'
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    return jsonify(data)


@app.route('/benefits-v2/missions/', defaults={'id': ''}, methods=["GET"])
@app.route('/benefits-v2/missions/<id>', methods=["GET"])
def missions(id):
    query = urlparse(request.url).query
    url = f'{API_URL}/missions/{id}?{query}'
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    return jsonify(data)


@app.route('/benefits-v2/notifications/', defaults={'id': ''}, methods=["GET"])
@app.route('/benefits-v2/notifications/<id>', methods=["GET"])
def notifications(id):
    query = urlparse(request.url).query
    url = f'{API_URL}/missions/{id}?{query}'
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    return jsonify(data)


def is_port_in_use(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


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
        app.run(debug=True)

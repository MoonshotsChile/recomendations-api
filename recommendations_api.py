import os
from flask import Flask
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app)


@app.route('/recommendations-api', methods=['GET'])
def suggestions_api():
    return {}


def is_port_in_use(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


def run_server(_port):
    serve(app, host='0.0.0.0', port=_port)


if __name__ == '__main__':
    port = 5001
    if os.environ.get("PYTHON_ENV") == "prod":
        if not is_port_in_use(port):
            run_server(port)
        else:
            print(f"port {port} is already in use, see ya ;)")
    else:
        app.run(debug=True)

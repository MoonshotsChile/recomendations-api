import json
from urllib import request
from urllib.request import urlopen
from urllib.parse import urlparse
from flask import jsonify
from constants import API_URL


class Userdata:
    @staticmethod
    def get(_request, _id=''):
        query = urlparse(_request.url).query
        url = f'{API_URL}/userdata/{_id}?{query}'
        json_url = urlopen(url)
        data = json.loads(json_url.read())
        return jsonify(data)

    @staticmethod
    def patch(_request, _id):
        url = f'{API_URL}/userdata/{_id}'
        req = request.Request(url, method='PATCH', data=_request.data)
        req.add_header('Content-Type', 'application/json')
        json_url = urlopen(req)
        data = json.loads(json_url.read())
        return data

    @staticmethod
    def add(_request, _id):
        url = f'{API_URL}/userdata/{_id}'
        req = request.Request(url, method='POST', data=_request.data)
        req.add_header('Content-Type', 'application/json')
        json_url = urlopen(req)
        data = json.loads(json_url.read())
        return jsonify(data)

    @staticmethod
    def delete(_request, _id):
        url = f'{API_URL}/userdata/{_id}'
        req = request.Request(url, method='DELETE')
        req.add_header('Content-Type', 'application/json')
        json_url = urlopen(req)
        data = json.loads(json_url.read())
        return jsonify(data)

import json
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

from flask import Flask
from flask import jsonify
from flask_cors import CORS

import mal_client

app = Flask(__name__)
CORS(app, origins=['https://twitch.tv', 'https://localhost:8080'])


@app.route('/<profile>/anime/top')
def get_top_anime(profile):
    return jsonify(mal_client.get_top_3_rated_anime(profile))

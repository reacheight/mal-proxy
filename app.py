from flask import Flask, jsonify, request
from flask_cors import CORS

import config
import mal_client

app = Flask(__name__)
CORS(app, origins=['https://twitch.tv', 'https://localhost:8080'])


@app.route('/<profile>/anime/top')
def get_top_anime(profile):
    limit = request.args.get('limit', config.DEFAULT_ANIME_LIMIT)
    return jsonify(mal_client.get_top_rated_anime(profile, limit))

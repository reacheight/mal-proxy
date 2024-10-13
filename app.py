from flask import Flask, jsonify, request
from flask_cors import CORS

import config
import mal_client
import mal_scrapper
app = Flask(__name__)
CORS(app, origins=['https://twitch.tv', r'.*\.ext-twitch\.tv', 'https://localhost:8080'])


@app.route('/<profile>')
def get_user_info(profile):
    return jsonify(mal_scrapper.get_user_info(profile))


@app.route('/<profile>/anime/top')
def get_top_anime(profile):
    limit = request.args.get('limit', config.DEFAULT_ANIME_LIMIT)
    return jsonify(mal_client.top_rated_anime(profile, limit))


@app.route('/<profile>/anime/recently-finished')
def get_recently_finished_anime(profile):
    limit = request.args.get('limit', config.DEFAULT_ANIME_LIMIT)
    return jsonify(mal_client.recently_finished_anime(profile, limit))


@app.route('/<profile>/anime/watching')
def get_watching_anime(profile):
    limit = request.args.get('limit', config.DEFAULT_ANIME_LIMIT)
    return jsonify(mal_client.watching_anime(profile, limit))

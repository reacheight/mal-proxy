from flask import Flask

import mal_client

app = Flask(__name__)


@app.route('/<profile>/anime/top')
def get_top_anime(profile):
    return mal_client.get_top_3_rated_anime(profile)

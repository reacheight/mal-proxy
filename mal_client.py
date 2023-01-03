import os

import requests

import config


def get_top_rated_anime(profile, limit=config.DEFAULT_ANIME_LIMIT):
    url = f'{config.MAL_HOST}/v2/users/{profile}/animelist?status=completed&sort=list_score&limit={limit}&fields=list_status'
    client_id = os.environ.get('MAL_CLIENT_ID')
    response = requests.get(url, headers={'X-MAL-CLIENT-ID': client_id})
    response.raise_for_status()

    anime_data = response.json()['data']
    anime_list = [
        build_user_anime(data['node']['id'], data['node']['title'], data['node']['main_picture']['medium'], data['list_status']['score'])
        for data in anime_data]
    return anime_list


def build_user_anime(anime_id, title, picture, score):
    return {
        'id': anime_id,
        'title': title,
        'picture': picture,
        'score': score
    }

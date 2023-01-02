import os

import requests


def get_top_3_rated_anime(profile):
    url = f'https://api.myanimelist.net/v2/users/{profile}/animelist?status=completed&sort=list_score&limit=3&fields=list_status'
    client_id = os.environ.get('MAL_CLIENT_ID')
    response = requests.get(url, headers={'X-MAL-CLIENT-ID': client_id})
    response.raise_for_status()

    anime_data = response.json()['data']
    anime_list = [build_user_anime(data['node']['title'], data['node']['main_picture']['medium'], data['list_status']['score']) for data in anime_data]
    return anime_list


def build_user_anime(title, picture, score):
    return {
        'title': title,
        'picture': picture,
        'score': score
    }

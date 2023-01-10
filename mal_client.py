import os
import requests

import config


def top_rated_anime(profile, limit=config.DEFAULT_ANIME_LIMIT):
    url = build_url(profile, 'completed', 'list_score', limit)
    return make_request(url)


def recently_finished_anime(profile, limit=config.DEFAULT_ANIME_LIMIT):
    url = build_url(profile, 'completed', 'list_updated_at', limit)
    return make_request(url)


def watching_anime(profile, limit=config.DEFAULT_ANIME_LIMIT):
    url = build_url(profile, 'watching', 'list_updated_at', limit)
    return make_request(url)


def make_request(url):
    client_id = os.environ.get('MAL_CLIENT_ID')
    response = requests.get(url, headers={'X-MAL-CLIENT-ID': client_id})
    response.raise_for_status()

    return map_response_to_anime_list(response.json())


def build_url(profile, status, sort, limit):
    return f'{config.MAL_HOST}/v2/users/{profile}/animelist?status={status}&sort={sort}&limit={limit}&fields=list_status'


def map_response_to_anime_list(json):
    data = json['data']
    anime_list = [
        build_user_anime(entry['node']['id'], entry['node']['title'], entry['node']['main_picture']['medium'],
                         entry['list_status']['score'], entry['list_status']['num_episodes_watched'])
        for entry in data]

    return anime_list


def build_user_anime(anime_id, title, picture, score, episodes_watched):
    return {
        'id': anime_id,
        'title': title,
        'picture': picture,
        'score': score,
        'episodes_watched': episodes_watched
    }

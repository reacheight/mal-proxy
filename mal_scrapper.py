import requests
from bs4 import BeautifulSoup

def get_user_info(username):
    url = f'https://myanimelist.net/profile/{username}'
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    user_profile_div = soup.find('div', class_='user-profile')
    img_element = user_profile_div.find('img')
    joined_li = next(
        (li for li in user_profile_div.find_all('li', class_='clearfix')
        if li.find('span', class_='user-status-title') and li.find('span', class_='user-status-title').string == 'Joined'),
        None
    )
    joined_element = joined_li.find('span', class_='user-status-data').string if joined_li else None

    return { 'pic': img_element['data-src'] if img_element else None, 'joined': joined_element }
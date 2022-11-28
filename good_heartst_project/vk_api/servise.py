
import requests
from psycopg2 import Error
import time
import json
import pandas as pd

import psycopg2
from psycopg2 import Error


def take_1000_posts():
    tocken = 'b94b8e22b94b8e22b94b8e224aba5a082abb94bb94b8e22da3c0c44a46cb96d0735fcd2'
    version = 5.131
    domen = 'elista_kalmykia'
    offset = 0
    all_post = []
    count = 100

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': tocken,
                                    'v': version,
                                    'domain': domen,
                                    'count': count,
                                    'offset': offset
                                }
                                )
        data = response.json()['response']['items']
        offset += 100
        all_post.extend(data)
        time.sleep(0.5)
    return all_post


all_post = take_1000_posts()


def parser_json(all_post):
    """Функция проходит по посту и забирает необходимые данные для бд."""
    result_list = list()
    # print(data, type(data))
    for item in all_post:
        post_dict = dict()
        post_dict['id'] = item['id']
        post_dict['date'] = item['date']
        post_dict['text_post'] = item['text']
        result_list.append(post_dict)
    return result_list


result_list = parser_json(all_post)
df = pd.DataFrame(data=result_list)
dog = df[df['text_post'].str.contains(r'\bсоб')]
cat = df[df['text_post'].str.contains(r'\bко')]
dfcat = pd.DataFrame(data=cat)
a = dfcat[dfcat['text_post'].str.contains(r'\bищу')]
bj = dfcat[dfcat['text_post'].str.contains(r'\bищ')]

dog_1 = df[df['text_post'].str.contains(r'\bпомо')]
dfdog = pd.DataFrame(data=dog)
dogfind = dfdog[dfdog['text_post'].str.contains(r'\bищ')]
dogfind1 = dfdog[dfdog['text_post'].str.contains(r'\bищ')]
help = df[df['text_post'].str.contains(r'\bпомо')]


import requests
from psycopg2 import Error
import time
import json
import pandas as pd

import psycopg2
from psycopg2 import Error

# class Parser_vk_json_to_psql():
#     def __init__ ():

def take_1000_posts():
    tocken = 'b94b8e22b94b8e22b94b8e224aba5a082abb94bb94b8e22da3c0c44a46cb96d0735fcd2'
    version = 5.131
    domen = 'elista_kalmykia'
    offset = 0
    all_post = []
    count= 100 

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



# def create_psql_table():
#     dog = '''CREATE TABLE [IF NOT EXISTS] DOG (
#        ID INT PRIMARY KEY NOT NULL,
#        PET TEXT NOT NULL,
#     );'''
#     cat = '''CREATE TABLE [IF NOT EXISTS] DOG (
#        ID INT PRIMARY KEY NOT NULL,
#        PET TEXT NOT NULL,
#     );'''
#     cat_find =  '''CREATE TABLE [IF NOT EXISTS] DOG (
#        ID INT PRIMARY KEY NOT NULL,
#        PET TEXT NOT NULL,
#     );'''
#     dog_find = '''CREATE TABLE [IF NOT EXISTS] DOG (
#        ID INT PRIMARY KEY NOT NULL,
#        PET TEXT NOT NULL,'''
#     try:
#         # Подключение к существующей базе данных
#         connection = psycopg2.connect(user="postgres",
#                                     # пароль, который указали при установке PostgreSQL
#                                     password="1111",
#                                     host="127.0.0.1",
#                                     port="5432",
#                                     database="postgres_db")
#         cursor = connection.cursor()
#         dog ="""INSER INTO dog """
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
#     finally:
#         if connection:
#             cursor.close()
#         connection.close()
#         print("Соединение с PostgreSQL закрыто")




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
    return print(result_list)


def sort_in_table(result_list):
    df = pd.DataFrame(data=result_list)
    dog = df[df['text_post'].str.contains(r'\bсоб')]
    cat = df[df['text_post'].str.contains(r'\bко')]
    dfcat = pd.DataFrame(data=cat)
    a = dfcat[dfcat['text_post'].str.contains(r'\bищу')]
    bj = dfcat[dfcat['text_post'].str.contains(r'\bищ')]

    dog_1=df[df['text_post'].str.contains(r'\bпомо')]
    dfdog = pd.DataFrame(data=dog)
    dogfind = dfdog[dfdog['text_post'].str.contains(r'\bищ')]
    dogfind1 = dfdog[dfdog['text_post'].str.contains(r'\bищ')]
    help_1 = df[df['text_post'].str.contains(r'\bпомо')]


def cat_find(result_list):
    try:
        connection = psycopg2.connect(user="postgres",
                                    # пароль, который указали при установке PostgreSQL
                                    password="1111",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres_db")
        connection.autocommit = True
        cursor = connection.cursor()
    except psycopg2.Error as e:
        return e
    with cursor:
        request_sql = """INSERT INTO CAT (id, text) WHERE text LIKE 'ко%' ""
                      VALUES (%s, %s) 
                      ON CONFLICT (id) DO NOTHING;"""
        for element in result_list:
            try:
                cursor.execute(request_sql, (element['id'],
                                             element['text_post']))
            except psycopg2.Error as e:
                return e
    with cursor:
        request_sql = """INSERT INTO DOG (id, text) WHERE text LIKE 'соб%' ""
                      VALUES (%s, %s) 
                      ON CONFLICT (id) DO NOTHING;"""
        for element in result_list:
            try:
                cursor.execute(request_sql, (element['id'],
                                             element['text_post']))
            except psycopg2.Error as e:
                return e






if __name__ == "__main__":
    all_post = take_1000_posts()
    result_list = parser_json(all_post)
   
    cat_find = cat_find(result_list)


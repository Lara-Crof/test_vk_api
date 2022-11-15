import json
import psycopg2

import vk_api
from vk_api.execute import VkFunction


vk_get_wall_posts = VkFunction(args=('values',), code='''
    return API.wall.get(%(values)s)['items'];
''')


def main():
    """Взятие постов из vk group"""
    login, password = '+79372111363', 'заяцнупогоди1239'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as e:
        print(e)
        return

    vk = vk_session.get_api()
    data = vk_get_wall_posts(vk, {'domain': 'elista_kalmykia', 'count': 2})

    return data


def load_to_file(data):
    """Запись считанных постов в json файл"""
    with open('wall.json', 'w', encoding='utf-8') as f:
        data = json.dumps(data)
        f.write(data)
    return None


def parser_attachments(some_dict):
    """Функция проходит по приложению поста."""
    for item in some_dict:
        return item['photo']['sizes'][4]['url']


def parser_josn(data):
    """Функция проходит по посту и забирает необходимые данные для бд."""
    result_list = list()
    for item in data:
        post_dict = dict()
        post_dict['id'] = item['id']
        post_dict['date'] = item['date']
        post_dict['text_post'] = item['text']
        try:
            post_dict['photo'] = parser_attachments(item['attachments'])
        except:
            post_dict['photo'] = ''
        result_list.append(post_dict)

    return result_list


def load_to_data_base(data):
    connect = psycopg2.connect(dbname='postgres',
                               user='postgres',
                               password='postgres',
                               host='localhost',
                               port='5433', )

    print("Database opened successfully")
    cur = connect.cursor()
    try:
        cur.execute("""CREATE TABLE test_vk_new
        (id INT NOT PRIMARY KEY,
        date CHAR(50) NOT NULL,
        test_post TEXT NOT NULL,
        photo TEST);""")
        connect.rollback()
    except psycopg2.ProgrammingError:
        print('Allready exists')
    with open('wall.json') as file:
        """ВОТ ЭТО ВСЁ НЕ РАБОТАЕТ НИФИГА
        record_to_bd = file.read()

        sql = 'INSERT INTO test_vk_new (id, date, test_post, photo) VALUES (%s, %s, %s, %s);' #ON CONFLICT (id) DO NOTHING;
        for element in data:
            try:
                print(type(element['']))
                cur.execute(sql, (element['id'],
                                  element['date'],
                                  element['text_post'],
                                  element['photo'])
                            )
                connect.rollback()
            except psycopg2.Error as e:
                print(f'Ошибка в хз чём 3 день ебусь! {e}')

        # cur.execute('SELECT * FROM test_3;')
        # rows = cur.fetchall()
        # for row in rows:
        #     print(row)
        # connect.close()
        """


if __name__ == '__main__':
    data = main()
    data = parser_josn(data)
    load_to_file(data)
    load_to_data_base(data)

# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests

import data

def post_products_kits(products_ids):

    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, headers=data.headers, json=products_ids)
response = post_products_kits(data.product_ids)

print(response.status_code)
print(response.json())

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH,

                         headers=data.headers)



print(response.status_code)

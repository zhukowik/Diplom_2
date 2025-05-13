import requests
import allure
from data import Url


class UserMethods:

    @staticmethod
    @allure.step('Создание пользователя: POST /api/auth/register')
    def create_new_user(payload):
        email = payload['email']
        password = payload['password']
        name = payload['name']
        return requests.post(Url.CREATE_USER, data=payload), email, password, name

    @staticmethod
    @allure.step('Создание пользователя: POST /api/auth/register')
    def create_user(email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return requests.post(Url.CREATE_USER, data=payload)

    @staticmethod
    @allure.step('Удаление пользователя: DELETE /api/auth/user')
    def delete_user(access_token):
        return requests.delete(Url.DELETE_USER, headers={'authorization': access_token})


    @staticmethod
    @allure.step("Авторизация пользователя: POST /api/auth/login")
    def login_user(email, password):
        payload = {
            "email": email,
            "password": password,
        }
        return requests.post(Url.LOGIN_USER, data=payload)

    @staticmethod
    @allure.step("Изменение данных пользователя: PATCH /api/auth/user")
    def changing_data(key, value, access_token):
        payload = {
            key : value
        }
        return requests.patch(Url.CHANGING_DATA_USER,data=payload, headers={'authorization': access_token})
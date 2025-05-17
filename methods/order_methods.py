import allure
import requests

from data import Url


class OrderMethods:

    @staticmethod
    @allure.step("Создание заказа: POST /api/orders")
    def create_order(access_token, ingredient_hash):
        order_body = {"ingredients": [ingredient_hash]}
        return requests.post(Url.CREATE_ORDER, data=order_body, headers={'authorization': access_token})

    @staticmethod
    @allure.step("Получение заказов конкретного пользователя: GET /api/orders")
    def get_list_order_user(access_token):
        return requests.get(Url.GET_LIST_ORDER, headers={'authorization': access_token})
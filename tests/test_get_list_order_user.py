import allure

from data import DataOrder
from methods.order_methods import OrderMethods


class TestGetListOrderUser:
    @allure.title("Проверка получения заказов конкретного пользователя")
    def test_get_list_order_user(self, login_user):
        response = OrderMethods.get_list_order_user(login_user[2])
        status_code = response.status_code
        response = response.json()
        assert status_code == 200
        assert response['orders'] == []

    @allure.title("Проверка получения заказов конкретного пользователя")
    def test_get_list_order_user(self):
        response = OrderMethods.get_list_order_user("")
        status_code = response.status_code
        response = response.json()
        assert status_code == 401
        assert response == DataOrder.RESPONSE_GET_ORDERS_NO_LOGIN
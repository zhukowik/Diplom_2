import allure

from data import DataOrder
from methods.order_methods import OrderMethods


class TestCreateOrder:
    @allure.title("Проверка создания заказа авторизованного пользователя")
    def test_create_order_login_user(self, login_user):
        response = OrderMethods.create_order(login_user[2], DataOrder.INGREDIENT_HASH)
        status_code = response.status_code
        response = response.json()
        assert status_code == 200
        assert response["name"] == "Краторный бургер"

    @allure.title("Проверка ошибки создания заказа не авторизованного пользователя")
    def test_create_order_no_login_user(self, login_user):
        response = OrderMethods.create_order("", DataOrder.INGREDIENT_HASH)
        status_code = response.status_code
        response = response.json()
        assert status_code == 200
        assert response["name"] == "Краторный бургер"

    @allure.title("Проверка создания заказа c ингредиентами")
    def test_create_order_with_ingredients(self, login_user):
        response = OrderMethods.create_order(login_user[2], DataOrder.INGREDIENT_HASH)
        status_code = response.status_code
        response = response.json()
        assert status_code == 200
        assert response["name"] == "Краторный бургер"

    @allure.title("Проверка создания заказа без ингредиентов")
    def test_create_order_without_ingredients(self, login_user):
        response = OrderMethods.create_order(login_user[2], "")
        status_code = response.status_code
        response = response.json()
        assert status_code == 400
        assert response == DataOrder.RESPONSE_CREATE_ORDER_WITHOUT_INGREDIENTS

    @allure.title("Проверка создания заказа c неверным хешем ингредиента")
    def test_create_order_without_ingredients(self, login_user):
        response = OrderMethods.create_order(login_user[2], DataOrder.INCORRECT_INGREDIENT_HASH)
        status_code = response.status_code
        assert status_code == 500

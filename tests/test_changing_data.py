import allure
import pytest

import generators_data
from data import DataUser
from methods.user_methods import UserMethods


class TestChangingData:
    @allure.title("Проверка изменения данных c авторизованным пользователем")
    @pytest.mark.parametrize("key, value", [("email", generators_data.GenerateData.FAKE_EMAIL),
                                            ("name", generators_data.GenerateData.FAKE_NAME)])
    def test_changing_data_user(self, login_user, key, value):
        UserMethods.login_user(login_user[0], login_user[1])
        response = UserMethods.changing_data(key, value, login_user[2])
        status_code = response.status_code
        response = response.json()
        assert status_code == 200
        assert response['user'][key] == value

    @allure.title("Проверка изменения данных c авторизованным пользователем")
    @pytest.mark.parametrize("key, value", [("email", generators_data.GenerateData.FAKE_EMAIL),
                                            ("name", generators_data.GenerateData.FAKE_NAME)])
    def test_changing_data_not_login_user(self, login_user, key, value):
        response = UserMethods.changing_data(key, value, login_user[2])
        status_code = response.status_code
        response = response.json()
        assert status_code == 401
        assert response == DataUser.RESPONSE_CHANGING_DATA_NO_LOGIN



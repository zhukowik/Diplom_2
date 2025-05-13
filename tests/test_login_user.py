import allure

from data import DataUser
from methods.user_methods import UserMethods


class TestLoginUser:
    @allure.title("Проверка авторизации успешной авторизации пользователя")
    def test_login_successful_user(self, generate_user_data):
        response = UserMethods.login_user(generate_user_data[2], generate_user_data[3])
        status_code = response.status_code
        response = response.json()
        assert status_code == 200
        assert response['success'] == True

    @allure.title("Проверка ошибки авторизации с неверным паролем и логином")
    def test_login_false_password_and_login(self):
        response = UserMethods.login_user(DataUser.EMAIL_USER, DataUser.PASSWORD_USER)
        status_code = response.status_code
        response = response.json()
        assert status_code == 401
        assert response == DataUser.RESPONSE_LOGIN_FALSE_PASSWORD_AND_LOGIN
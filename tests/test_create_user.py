import allure

from data import DataUser
from methods.user_methods import UserMethods


class TestCreateUser:
    @allure.title("Проверка создания уникального пользователя")
    def test_create_unique_user(self, generate_user_data):
        body = generate_user_data[0]
        status_code = generate_user_data[1]
        assert status_code == 200
        assert  body['success'] == True

    @allure.title("Проверка ошибки создания уже зарегистрированного пользователя")
    def test_create_of_already_registered_user(self, generate_user_data):
        response = UserMethods.create_user(generate_user_data[2],generate_user_data[3],generate_user_data[4])
        status_code = response.status_code
        response = response.json()
        assert status_code == 403
        assert response == DataUser.RESPONSE_CREATE_OF_ALREADY_REGISTERED_USER

    @allure.title("Проверка создания пользователя и не заполнить одно из обязательных полей")
    def test_create_need_to_pass_required_fields_to_handle(self):
        response = UserMethods.create_user(DataUser.EMAIL_USER, DataUser.PASS_FIELD, DataUser.NAME_USER)
        status_code = response.status_code
        response = response.json()
        assert status_code == 403
        assert  response == DataUser.RESPONSE_CREATE_USER_PASS_FIELD

    
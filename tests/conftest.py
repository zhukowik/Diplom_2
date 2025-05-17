
import pytest

from generators_data import GeneratePayload
from methods.user_methods import UserMethods


@pytest.fixture()
def generate_user_data():
    user_body = GeneratePayload.generate_user_payload()
    email = user_body['email']
    password = user_body['password']
    name = user_body['name']
    new_user = UserMethods.create_new_user(user_body)
    response = new_user[0].json()
    status_code = new_user[0].status_code
    yield [response, status_code, email, password, name]
    access_token = response['accessToken']
    UserMethods.delete_user(access_token)

@pytest.fixture()
def login_user():
    user_body = GeneratePayload.generate_user_payload()
    new_user = UserMethods.create_new_user(user_body)
    email = user_body['email']
    password = user_body['password']
    response = new_user[0].json()
    access_token = response['accessToken']
    yield [email, password, access_token]
    UserMethods.delete_user(access_token)



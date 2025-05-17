


class Url:
    MAIN_SITE = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = f'{MAIN_SITE}/api/auth/register'
    LOGIN_USER = f'{MAIN_SITE}/api/auth/login'
    CHANGING_DATA_USER = f'{MAIN_SITE}/api/auth/user'
    CREATE_ORDER = f'{MAIN_SITE}/api/orders'
    GET_LIST_ORDER = f'{MAIN_SITE}/api/orders'
    DELETE_USER = f'{MAIN_SITE}/api/auth/user'


class DataUser:
    USER_BODY = {
        "email": "test-user@mail.ru",
        "password": "1234qwerasdf",
    }

    RESPONSE_CREATE_OF_ALREADY_REGISTERED_USER = {
        "success": False,
        "message": "User already exists"
    }

    RESPONSE_CREATE_USER_PASS_FIELD = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    RESPONSE_LOGIN_FALSE_PASSWORD_AND_LOGIN = {
        "success": False,
        "message": "email or password are incorrect"
    }

    RESPONSE_CHANGING_DATA_NO_LOGIN = {
        "success": False,
        "message": "You should be authorised"
    }




    PASS_FIELD = ""
    EMAIL_USER = "TEST_API@Mmail.ru"
    PASSWORD_USER = "][po';lk"
    NAME_USER = "Zewer"



class DataOrder:

    INGREDIENT_HASH = "61c0c5a71d1f82001bdaaa6c"
    INCORRECT_INGREDIENT_HASH = "609646e4dc916e00276b2870"

    RESPONSE_CREATE_ORDER_WITHOUT_INGREDIENTS = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }

    RESPONSE_GET_ORDERS_NO_LOGIN = {
        "success": False,
        "message": "You should be authorised"
    }

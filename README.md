## Дипломный проект. Задание 2: API-тесты
<hr>

## Студент: Жуков Артём


<hr>

## <h>Project: STELLAR BURGER API</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest -v

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла      | Содержание файла                        |
|---------------------|-----------------------------------------|
| Tests dir           | Директория с тестами                    |
| test_create_user.py | Тесты на создание пользователя          |
| test_login_user.py  | Тесты на авторизацию пользователя       |
| conftest.py         | Фикстуры                                |
| data.py             | Файл с URL и body запросов              |
| order_methods.py    | http клиент к order методам             |
| user_methods.py     | http клиент к user методам              |
| generators_data.py  | Генератор данных                        |
| requirements.txt    | Файл с зависимостями                    |
| allure_results.dir  | Папка с отчетами Allure                 |
| allure_results.dir  | Папка с отчетами Allure                 |
 test_create_order.py  | Тесты на создание пользователя          |
 test_changing_data.py  | Тесты на изменение данных пользователя  |
 test_get_list_orders.py  | Тесты на получение заказов пользователя |

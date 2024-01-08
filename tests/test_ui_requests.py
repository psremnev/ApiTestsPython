import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from helper import open_page, get_error_message
from constants import Endpoints
from app_settings import app_settings, test_app_id
from pages.Requests import Requests
from tests.data.test_data import responses, requests_titles
import json


class TestUIRequests:
    """Тесты запросов из UI"""
    driver = None
    requests = None

    def setup_class(self):
        self.driver = webdriver.Chrome()
        app = app_settings.get(test_app_id)
        open_page(self.driver, app.get('base_url'))
        self.requests = Requests(self.driver)

    def test_check_requests_titles(self):
        errors = []
        for index, endpoint in enumerate(self.requests.endpoints):
            current = endpoint.text
            test = requests_titles[index]
            if test != current:
                errors.append(get_error_message('Не соответствует эталону заголовок запроса', current, test))

        assert len(errors) == 0, f'{"".join(errors)}'

    @pytest.mark.parametrize('endpoints_name, res_test_data', [(Endpoints.USERS.value, responses.get('users')),
                                                                (Endpoints.UNKNOWN.value, responses.get('unknown')),
                                                                (Endpoints.REGISTER.value, responses.get('register')),
                                                                (Endpoints.LOGIN.value, responses.get('login'))])
    def test_check_requests(self, endpoints_name, res_test_data):
        errors = []
        # получаем все endpoints по категории
        endpoints = self.requests.get_endpoints_elements(endpoints_name)
        for index, endpoint in enumerate(endpoints):
            # Очищаем поле статуса - для мониторинга выполнения запроса
            self.driver.execute_script("document.querySelector('.response .response-code').innerHTML = ''")

            # Кликаем для выполнения запроса
            endpoint.click()

            # Проверяем что запрос выполнен, поле статуса должно заполнится
            WebDriverWait(self.driver, 4).until(lambda _: self.requests.status.text != '')

            # получаем тестовые данные
            test_data = res_test_data[index]
            test_status = test_data.get('status')
            test_path = test_data.get('path')
            test_name = test_data.get('name')
            test_response_keys = test_data.get('res_keys')

            # получаем данные из верстки
            current_status = self.requests.status.text
            current_path = self.requests.path.text
            current_response = self.requests.response.text and json.loads(self.requests.response.text)
            current_response_keys = current_response and current_response.keys()

            # проверяем данные на соответствие
            # статус
            if current_status != test_status:
                errors.append(
                    get_error_message(f'Точка входа: {endpoints_name}-{test_name}', current_status, test_status))

            # путь
            if current_path != test_path:
                errors.append(get_error_message(f'Путь запроса: {endpoints_name}-{test_name}', current_path, test_path))

            # поля в ответе
            if list(current_response_keys) != test_response_keys:
                errors.append(
                    get_error_message(f'В ответе запроса не хватает полей: {endpoints_name}-{test_name}',
                                      current_response_keys, test_response_keys))

        assert len(errors) == 0, f'Не верные данные в ответе на запрос:\n {"".join(errors)}'

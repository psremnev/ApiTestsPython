from datetime import datetime
import pytest
from services.Base import Base
from constants import Endpoints
from helper import get_error_message
from tests.data.test_data import responses
from tests.data.req_data import test_id, test_id_not_found, users, register, login, test_page_id
from app_settings import test_app_id

(user_list, user_single, user_not_found, user_create, user_update_put, user_update_patch, user_delete,
 user_delayed) = responses.get('users')
unknown_list, unknown_single, unknown_not_found = responses.get('unknown')
register_success, register_unsuccess = responses.get('register')
login_success, login_unsuccess = responses.get('login')


def get_service(endpoint):
    return Base(test_app_id, endpoint)


def keys_is_equal_test_keys(res, test_keys):
    res_keys = list(dict(res.json()).keys())
    return res_keys == test_keys, res_keys, test_keys


class TestApiRequests:
    """Тесты запросов"""

    @pytest.mark.parametrize('endpoint, res_test_data', [(Endpoints.USERS.value, user_list),
                                                         (Endpoints.UNKNOWN.value, unknown_list)])
    def test_get_list_data(self, endpoint, res_test_data):
        """Проверка списочных данных"""
        service = get_service(endpoint)
        res = service.get()
        test_status = res_test_data.get('status')
        current_status = str(res.status_code)
        msg = f'Точка входа: {endpoint}-list'
        assert current_status == test_status, get_error_message(msg, current_status, test_status)
        keys_equal_res, res_keys, test_keys = keys_is_equal_test_keys(res, res_test_data.get('res_keys'))
        assert keys_is_equal_test_keys(res, res_test_data.get('res_keys')), get_error_message(msg,
                                                                                              res_keys, test_keys)

    @ pytest.mark.parametrize('endpoint, res_test_data', [(Endpoints.USERS.value, user_list),
                                        (Endpoints.UNKNOWN.value, unknown_list)])
    def test_list_by_page(self, endpoint, res_test_data):
        """Проверка постраничных данных"""
        service = get_service(endpoint)
        res = service.get(params={'page': test_page_id})
        test_status = res_test_data.get('status')
        current_status = str(res.status_code)
        msg = f'Точка входа: {endpoint}-list'
        assert current_status == test_status, get_error_message(msg, current_status, test_status)
        keys_equal_res, res_keys, test_keys = keys_is_equal_test_keys(res, res_test_data.get('res_keys'))
        assert keys_is_equal_test_keys(res, res_test_data.get('res_keys')), get_error_message(msg,
                                                                                              res_keys, test_keys)

    @pytest.mark.parametrize('endpoint, res_test_data', [(Endpoints.USERS.value, user_single),
                                                         (Endpoints.UNKNOWN.value, unknown_single)])
    def test_get_single_data(self, endpoint, res_test_data, key=2):
        """Проверка получения одного элемента по id"""
        service = get_service(endpoint)
        res = service.get(key)
        test_status = res_test_data.get('status')
        current_status = str(res.status_code)
        msg = f'Точка входа: {endpoint}-single'
        assert current_status == test_status, get_error_message(msg, current_status, test_status)
        keys_equal_res, res_keys, test_keys = keys_is_equal_test_keys(res, res_test_data.get('res_keys'))
        assert keys_is_equal_test_keys(res, res_test_data.get('res_keys')), get_error_message(msg,
                                                                                              res_keys, test_keys)

    @pytest.mark.parametrize('endpoint, req_data, res_test_data',
                             [(Endpoints.USERS.value, users.get('create'),
                               user_create)])
    def test_create_single(self, endpoint, req_data, res_test_data):
        """Проверка создания элемента"""
        service = get_service(endpoint)
        res = service.post(data=req_data)
        test_status = res_test_data.get('status')
        current_status = str(res.status_code)
        msg = f'Точка входа: {endpoint}-create'
        assert current_status == test_status, get_error_message(msg, current_status, test_status)
        keys_equal_res, res_keys, test_keys = keys_is_equal_test_keys(res, res_test_data.get('res_keys'))
        assert keys_is_equal_test_keys(res, res_test_data.get('res_keys')), get_error_message(msg,
                                                                                              res_keys, test_keys)

    @pytest.mark.parametrize('endpoint, req_data, res_test_data',
                             [(Endpoints.USERS.value, users.get('update'),
                               user_update_put)])
    def test_update_put(self, endpoint, req_data, res_test_data, key=test_id):
        """Проверка полного обновления данных элемента"""
        service = get_service(endpoint)
        res = service.put(key=key, data=req_data)
        test_status = res_test_data.get('status')
        current_status = str(res.status_code)
        msg = f'Точка входа: {endpoint}-update_put'
        assert current_status == test_status, get_error_message(msg, current_status, test_status)
        keys_equal_res, res_keys, test_keys = keys_is_equal_test_keys(res, res_test_data.get('res_keys'))
        assert keys_is_equal_test_keys(res, res_test_data.get('res_keys')), get_error_message(msg,
                                                                                              res_keys, test_keys)

    @pytest.mark.parametrize('endpoint, req_data, res_test_data',
                             [(Endpoints.USERS.value, users.get('update'),
                               user_update_patch)])
    def test_update_patch(self, endpoint, req_data, res_test_data, key=test_id):
        """Проверка частичного обновления данных элемента"""
        service = get_service(endpoint)
        res = service.patch(key=key, data=req_data)
        test_status = res_test_data.get('status')
        current_status = str(res.status_code)
        msg = f'Точка входа: {endpoint}-update_patch'
        assert current_status == test_status, get_error_message(msg, current_status, test_status)
        keys_equal_res, res_keys, test_keys = keys_is_equal_test_keys(res, res_test_data.get('res_keys'))
        assert keys_is_equal_test_keys(res, res_test_data.get('res_keys')), get_error_message(msg,
                                                                                              res_keys, test_keys)

    @pytest.mark.parametrize('endpoint, res_test_data',
                             [(Endpoints.USERS.value, user_delete)])
    def test_delete(self, endpoint, res_test_data, key=test_id):
        """Проверка удаления элемента"""
        service = get_service(endpoint)
        res = service.delete(key=key)
        test_status = res_test_data.get('status')
        current_status = str(res.status_code)
        assert current_status == test_status, get_error_message(f'Точка входа: {endpoint}-delete',
                                                                current_status, test_status)
        

    @pytest.mark.parametrize('endpoint, res_test_data, delay',
                             [(Endpoints.USERS.value, user_list, 3)])
    def test_delayed(self, endpoint, res_test_data, delay):
        """Проверка получения списка элемнтов с задержкой"""
        st_time = datetime.now()
        service = get_service(endpoint)
        res = service.get(params={'delay': delay})
        time_sec = (datetime.now() - st_time).total_seconds()

        # Проверяем что время задержки вызова отработало корректно
        assert time_sec > delay, (f'Параметр задержки вызова работает не верно. Ожидание: больше {delay} секунд.'
                                  f' Текущее время: {time_sec}')

        # Проверяем статус
        test_status = res_test_data.get('status')
        current_status = str(res.status_code)
        assert current_status == test_status, get_error_message(f'Точка входа: {endpoint}-create',
                                                                current_status, test_status)
        msg = f'Точка входа: {endpoint}-delayed'
        assert current_status == test_status, get_error_message(msg, current_status, test_status)
        keys_equal_res, res_keys, test_keys = keys_is_equal_test_keys(res, res_test_data.get('res_keys'))
        assert keys_is_equal_test_keys(res, res_test_data.get('res_keys')), get_error_message(msg,
                                                                                              res_keys, test_keys)

    @pytest.mark.parametrize('endpoint, res_test_data', [(Endpoints.USERS.value, user_not_found),
                                                         (Endpoints.UNKNOWN.value, unknown_not_found)])
    def test_not_found(self, endpoint, res_test_data, not_found_id=test_id_not_found):
        """Проверка получения несуществующего элемента"""
        service = get_service(endpoint)
        res = service.get(key=not_found_id)
        test_status = res_test_data.get('status')
        current_status = str(res.status_code)
        msg = f'Точка входа: {endpoint}-not_found'
        assert current_status == test_status, get_error_message(msg, current_status, test_status)
        keys_equal_res, res_keys, test_keys = keys_is_equal_test_keys(res, res_test_data.get('res_keys'))
        assert keys_is_equal_test_keys(res, res_test_data.get('res_keys')), get_error_message(msg,
                                                                                              res_keys, test_keys)

    @pytest.mark.parametrize('req_data, res_test_data', [(register.get('success'), register_success),
                                                     (register.get('unsuccess'), register_unsuccess)])
    def test_register(self, req_data, res_test_data):
        """Проверка регистрации"""
        endpoint = Endpoints.REGISTER.value
        service = get_service(endpoint)
        res = service.post(data=req_data)
        test_status = res_test_data.get('status')
        current_status = str(res.status_code)
        msg = f'Точка входа: {endpoint}-register'
        assert current_status == test_status, get_error_message(msg, current_status, test_status)
        keys_equal_res, res_keys, test_keys = keys_is_equal_test_keys(res, res_test_data.get('res_keys'))
        assert keys_is_equal_test_keys(res, res_test_data.get('res_keys')), get_error_message(msg,
                                                                                              res_keys, test_keys)

    @pytest.mark.parametrize('req_data, res_test_data', [(login.get('success'), login_success),
                                                         (login.get('unsuccess'), login_unsuccess)])
    def test_login(self, req_data, res_test_data):
        """Проверка логина"""
        endpoint = Endpoints.LOGIN.value
        service = get_service(endpoint)
        res = service.post(data=req_data)
        test_status = res_test_data.get('status')
        current_status = str(res.status_code)
        msg = f'Точка входа: {endpoint}-login'
        assert current_status == test_status, get_error_message(msg, current_status, test_status)
        keys_equal_res, res_keys, test_keys = keys_is_equal_test_keys(res, res_test_data.get('res_keys'))
        assert keys_is_equal_test_keys(res, res_test_data.get('res_keys')), get_error_message(msg,
                                                                                              res_keys, test_keys)

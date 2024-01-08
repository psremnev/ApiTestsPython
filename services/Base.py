import requests
from app_settings import app_settings


class Base:
    _service_address = None

    def __init__(self, test_app_id, endpoint):
        app = app_settings.get(test_app_id)
        self._service_address = f'{app.get("base_url")}/{app.get("api_path")}/{endpoint}'

    def get(self, key=None, params=None):
        return requests.get(self.__get_url(key), params=params)

    def post(self, key=None, params=None, data=None):
        return requests.post(self.__get_url(key), params=params, data=data)

    def put(self, key=None, params=None, data=None):
        return requests.put(self.__get_url(key), params=params, data=data)

    def patch(self, key=None, params=None, data=None):
        return requests.patch(self.__get_url(key), params=params, data=data)

    def delete(self, key=None, params=None, data=None):
        return requests.delete(self.__get_url(key), params=params, data=data)

    def __get_url(self, key=None):
        return (key and f'{self._service_address}/{key}') or self._service_address

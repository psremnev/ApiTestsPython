from enum import Enum


class ElementAttribute(Enum):
    HREF = 'href'


class Endpoints(Enum):
    USERS = 'users'
    UNKNOWN = 'unknown'
    REGISTER = 'register'
    LOGIN = 'login'


class StatusCode(Enum):
    OK = '200'
    NOT_FOUND = '404'
    CREATED = '201'
    OK_NO_BODY = '204'
    BAD_REQUEST = '400'

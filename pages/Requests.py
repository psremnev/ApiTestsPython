from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from constants import ElementAttribute, Endpoints


class Requests:
    """Блок запросов на главной странице"""
    endpoints = None
    status = None
    path = None
    response = None

    def __init__(self, driver):
        self.driver = driver
        self.init_elements()

    def init_elements(self):
        self.endpoints = self.driver.find_elements(By.CSS_SELECTOR, '.endpoints a')
        self.path = self.driver.find_element(By.CSS_SELECTOR, '.request .url')
        self.status = self.driver.find_element(By.CSS_SELECTOR, '.response .response-code')
        self.response = self.driver.find_element(By.CSS_SELECTOR, '.response pre')

    def get_endpoints_elements(self, endpoints_name):
        return [user for user in self.endpoints if user.get_attribute(ElementAttribute.HREF.value)
        .__contains__(endpoints_name)]

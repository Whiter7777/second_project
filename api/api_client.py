from configurations.configuration import ConfigManager
import allure
from httpx import Client


class ApiIClient(Client):
    def __init__(self, base_url):
        super().__init__(base_url=base_url)

    @allure.step('Making GET request to "{url}"')
    def get(self, url, params=None):
        return super().get(url=url, params=params)

    @allure.step('Making POST request to "{url}"')
    def post(self, url, json=None):
        return super().post(url=url, json=json)

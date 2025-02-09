import allure
from httpx import Client, Response

class HTTPClient(Client):
    @allure.step('Making GET request to "{url}"')
    def get(self, url) -> Response:
        return super().get(url=url)

    @allure.step('Making POST request to "{url}"')
    def post(self, url) -> Response:
        return super().post(url=url)


class APIClient:
    def __init__(self, client: HTTPClient) -> None:
        self._client = client

    @property
    def client(self):
        return self._client


response = HTTPClient().get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Ошибка:", response.status_code)
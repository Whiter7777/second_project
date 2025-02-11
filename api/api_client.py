from configurations.configuration import ConfigManager
import typing
import allure
from httpx import Client, Response
from httpx._client import UseClientDefault
from httpx._types import (AuthTypes, CookieTypes, HeaderTypes, QueryParamTypes,
                          RequestContent, RequestData, RequestExtensions,
                          RequestFiles, TimeoutTypes, URLTypes)

class HTTPClient(Client):
    @allure.step('Making GET request to "{url}"')
    def get(self, url) -> Response:
        return super().get(url=url)

    @allure.step('Making POST request to "{url}"')
    def post(self, url) -> Response:
        return super().post(url=url)
#
# class APIClient:
#     def __init__(self, client: HTTPClient) -> None:
#         self._client = client
#
#     @property
#     def client(self):
#         return self._client

class ApiIClient(Client):
    def __init__(self):
        super().__init__(base_url=ConfigManager().get_config_data().baseUrl)

    @allure.step('Making GET request to "{url}"')
    def get(self, url: URLTypes, *,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        return super().get(url=url, params=params, headers=headers, cookies=cookies,
            auth=auth, follow_redirects=follow_redirects, timeout=timeout,
            extensions=extensions)

    @allure.step('Making POST request to "{url}"')
    def post(self, url: URLTypes, *,
        content: typing.Optional[RequestContent] = None,
        data: typing.Optional[RequestData] = None,
        files: typing.Optional[RequestFiles] = None,
        json: typing.Optional[typing.Any] = None,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        return super().post(url=url, content=content, data=data, files=files,
            json=json, params=params, headers=headers, cookies=cookies, auth=auth,
            follow_redirects=follow_redirects, timeout=timeout, extensions=extensions)

response = HTTPClient().get("https://jsonplaceholder.typicode.com/posts/99")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Ошибка:", response.status_code)
import pytest
from http import HTTPStatus
from api.api_client import ApiIClient
from api.builder import Builder
from assertions.assertion_base import AssertionBase
from configurations.configuration import ConfigManager
from configurations.test_manager import TestManager
from models.user_model import UserModel
from api.routes import Routes
from models.post_model import PostModel
from utilities.generate_random_post_object import RandomPostGenerator


class TestAPI:
    @pytest.fixture(scope='class')
    def client(self):
        return ApiIClient(ConfigManager().get_config_data().baseUrl)

    def test_get_messages(self, client):
        response = Builder().get_objects(client,
                                         Routes.POSTS)
        AssertionBase().assert_status_code(response, HTTPStatus.OK)
        AssertionBase().assert_schema(response, PostModel)

    def test_get_message(self, client):
        response = Builder().get_object(client,
                                        Routes.POSTS_ITEM,
                                        TestManager.get_test_data().message_id_real)
        AssertionBase().assert_status_code(response, HTTPStatus.OK)
        AssertionBase().assert_schema(response, PostModel)
        AssertionBase().assert_response_model(response,
                                           TestManager.get_test_data().message_id_99, PostModel)

    def test_post_not_exist(self, client):
        response = Builder().get_object(client,
                                        Routes.POSTS_ITEM,
                                        TestManager.get_test_data().message_id_unreal)
        AssertionBase().assert_status_code(response, HTTPStatus.NOT_FOUND)
        AssertionBase().assert_empty_body(response)

    def test_post_object_full(self, client):
        random_post = RandomPostGenerator().generate_random_post(
                                             TestManager().get_test_data().letters_quant_in_range,
                                             TestManager().get_test_data().userid_1)
        response = Builder().post_object(client,
                                         Routes.POSTS,
                                         json=random_post)
        AssertionBase().assert_status_code(response, HTTPStatus.CREATED)
        random_post["id"] = TestManager().get_test_data().id_101
        AssertionBase().assert_response_model(response, PostModel(**random_post), PostModel)

    def test_get_users(self, client):
        response = Builder().get_objects(client, Routes.USERS)
        AssertionBase().assert_status_code(response, HTTPStatus.OK)
        AssertionBase().assert_schema(response, UserModel)
        body = response.json()
        for item in body:
            if item["id"] == TestManager().get_test_data().user_id:
                assert TestManager.get_test_data().user_id_5 == UserModel(**item)
                return item

    def test_get_user(self, client):
        response = Builder().get_object(client,
                                        Routes.USERS_ITEM,
                                        TestManager.get_test_data().user_id)
        AssertionBase().assert_status_code(response, HTTPStatus.OK)
        AssertionBase().assert_schema(response, UserModel)
        assert response.json() == TestAPI().test_get_users(client)

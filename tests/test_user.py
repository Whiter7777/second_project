import pytest
from http import HTTPStatus
from api.api_client import ApiIClient
from api.builder import Builder
from assertions.assertion_base import AssertUser
from configurations.test_manager import TestManager
from models.user_model import Message, User
from utilities.generate_random_post_object import RandomPostGenerator


class TestUser:
    @pytest.fixture(scope='class')
    def client(self):
        return ApiIClient()

    def test_get_messages(self, client):
        response = Builder().get_objects(client,
                                         TestManager().get_test_data().all_messages)
        AssertUser().assert_status_code(response, HTTPStatus.OK)
        AssertUser().assert_schema(response, Message)

    def test_get_message(self, client):
        response = Builder().get_object(client,
                                        TestManager().get_test_data().all_messages_item,
                                        TestManager.get_test_data().message_id_real)
        AssertUser().assert_status_code(response, HTTPStatus.OK)
        AssertUser().assert_schema(response, Message)
        AssertUser().assert_response_model(response,
                                           TestManager.get_test_data().message_id_99, Message)

    def test_get_object_not_exist(self, client):
        response = Builder().get_object(client,
                                        TestManager().get_test_data().all_messages_item,
                                        TestManager.get_test_data().message_id_unreal)
        AssertUser().assert_status_code(response, HTTPStatus.NOT_FOUND)
        AssertUser().assert_empty_body(response)

    def test_post_object_full(self, client):
        random_post = RandomPostGenerator().generate_random_post(
                                             TestManager().get_test_data().letters_quant_in_range,
                                             TestManager().get_test_data().userid_1)
        response = Builder().post_object(client,
                                         TestManager().get_test_data().all_messages,
                                         json=random_post)
        AssertUser().assert_status_code(response, HTTPStatus.CREATED)
        AssertUser().assert_body_info(response, random_post["title"], random_post["body"], random_post["userId"])

    def test_get_users(self, client):
        response = Builder().get_objects(client,
                                         TestManager().get_test_data().all_users)
        AssertUser().assert_status_code(response, HTTPStatus.OK)
        AssertUser().assert_schema(response, User)
        body = response.json()
        for item in body:
            if item["id"] == TestManager().get_test_data().user_id:
                assert TestManager.get_test_data().user_id_5 == User(**item)
                return item

    def test_get_user(self, client):
        response = Builder().get_object(client,
                                        TestManager().get_test_data().all_users_item,
                                        TestManager.get_test_data().user_id)
        AssertUser().assert_status_code(response, HTTPStatus.OK)
        AssertUser().assert_schema(response, User)
        assert response.json() == TestUser().test_get_users(client)

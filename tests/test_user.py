import pytest
import json
from http import HTTPStatus
from api.api_client import ApiIClient
from api.builder import Builder
from assertions.assertion_base import AssertUser
from configurations.test_manager import TestManager
from models.user_model import Message

class TestUser:
    @pytest.fixture(scope='class')
    def client(self):
        return ApiIClient()

    def test_get_users(self, client, request):
        response = Builder().get_objects(client)
        AssertUser().assert_status_code(response, HTTPStatus.OK)

    def test_get_user(self, client, request):
        response = Builder().get_object(client, TestManager.get_test_data().message_id_real)
        data = response.json()
        assert data["userId"] == 10
        assert data["id"] == 99
        AssertUser().assert_status_code(response, HTTPStatus.OK)
        AssertUser().assert_schema(response, Message)

    def test_get_object_not_exist(self, client, request):
        response = Builder().get_object(client, 1593576458)

        AssertUser().assert_status_code(response, HTTPStatus.NOT_FOUND)
        # AssertUser().assert_not_exist(request, response, 1593576458)

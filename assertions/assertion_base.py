from typing import Type
from pydantic import BaseModel
from utilities.is_list_sorted import IsListSorted


class AssertUser:
    def assert_status_code(self, response, expected_code):
        assert expected_code == response.status_code

    def assert_schema(self, response, model: Type[BaseModel]):
        body = response.json()
        if isinstance(body, list):
            if IsListSorted().is_list_sorted(body, "id"):
                for item in body:
                    model.model_validate(item, strict=True)
        else:
            model.model_validate(body, strict=True)

    def assert_body_info(self, response, title: str, body: str, user_id: int, ):
        data = response.json()
        assert data["title"] == title and data["body"] == body and data["userId"] == user_id and data["id"]

    def assert_response_model(self, response, exp_body, model: Type[BaseModel]):
        actual_body = response.json()
        assert exp_body == model(**actual_body)

    def assert_empty_body(self, response):
        assert response.json() == {}

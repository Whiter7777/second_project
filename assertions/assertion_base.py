from typing import Type
from pydantic import BaseModel


class AssertUser:
    def assert_status_code(self, response, expected_code):
        assert expected_code == response.status_code

    def assert_schema(self, response, model: Type[BaseModel]):
        body = response.json()
        if isinstance(body, list):
            for item in body:
                model.model_validate(item, strict=True)
        else:
            model.model_validate(body, strict=True)
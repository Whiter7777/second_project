from pydantic import BaseModel


class ConfigModel(BaseModel):
    baseUrl: str

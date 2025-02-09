from pydantic import BaseModel


class Settings(BaseModel):
    baseUrl: str

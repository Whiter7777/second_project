from pydantic import BaseModel

class User(BaseModel):
    userID: int
    id: int
    title: str
    body: str
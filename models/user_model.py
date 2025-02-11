from pydantic import BaseModel

class TestModel(BaseModel):
    all_messages: str
    all_messages_item: str
    all_users: str
    all_users_item: str
    message_userid_real: int
    message_id_real: int
    message_id_unreal: int
    user_id: int

class Message(BaseModel):
    userId: int
    id: int
    title: str
    body: str

class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str

class Geo(BaseModel):
    lat: str
    lng: str

class Adress(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo

class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    adress: Adress
    phone: str
    website: str
    company: Company

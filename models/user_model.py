from pydantic import BaseModel


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


class Address(BaseModel):
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
    address: Address
    phone: str
    website: str
    company: Company


class TestModel(BaseModel):
    all_messages: str
    all_messages_item: str
    all_users: str
    all_users_item: str
    message_userid_real: int
    message_id_real: int
    message_id_unreal: int
    user_id: int
    userid_1: int
    letters_quant_in_range: tuple
    message_id_99: Message
    user_id_5: User

from pydantic import BaseModel


class CompanyModel(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class GeoModel(BaseModel):
    lat: str
    lng: str


class AddressModel(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: GeoModel


class UserModel(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: AddressModel
    phone: str
    website: str
    company: CompanyModel

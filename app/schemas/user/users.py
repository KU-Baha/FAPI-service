from bson import ObjectId
from typing import Optional
from pydantic import BaseModel, Field

from app.schemas.schemas import PyObjectId


class User(BaseModel):
    __tablename__ = "users"
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: str = Field(...)


class CreateUser(User):
    first_name: str = Field(...)
    last_name: str = Field(...)
    phone_number: str = Field(...)
    password: str = Field(...)
    repeat_password: str = Field(...)

    def is_valid(self):
        result = self.password == self.repeat_password
        self.__delattr__("repeat_password")
        return result

    class Config:
        json_encoders = {ObjectId: str}

        schema_extra = {
            "example": {
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jdoe@example.com",
                "phone_number": "+996999312292",
                "password": "admin12345",
                "repeat_password": "admin12345",
            }
        }


class SignInUser(User):
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "jdoe@example.com",
                "password": "some_password"
            }
        }


class UpdateUser(User):
    first_name: str = Field(...)
    last_name: str = Field(...)
    phone_number: str = Field(...)
    old_password: Optional[str] = ""
    new_password: Optional[str] = ""

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jdoe@example.com",
                "phone_number": "+996123123123",
            }
        }

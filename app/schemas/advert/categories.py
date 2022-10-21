from fastapi import File, UploadFile
from pydantic import BaseModel, Field

from app.schemas.schemas import PyObjectId


class Category(BaseModel):
    __tablename__ = "categories"
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(max_length=100)
    icon: UploadFile = File(...)

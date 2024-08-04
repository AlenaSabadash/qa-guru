from typing import List

from pydantic import BaseModel, EmailStr, Field

from src.models.users import UserModel


class UserResponse(BaseModel):
    id: int = Field(example=1)
    email: str = Field(example="john.doe@mail.com")
    first_name: str = Field(example="firstname")
    last_name: str = Field(example="lastname")


class UserListResponse(BaseModel):
    items: List[UserModel]


class UserCreate(BaseModel):
    email: EmailStr = Field(example="example@mail.com")
    first_name: str = Field(example="firstname")
    last_name: str = Field(example="lastname")

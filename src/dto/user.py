from dataclasses import dataclass

from fastapi import Query
from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserRead(BaseUser):
    id: int

    class Config:
        orm_mode = True


@dataclass
class UserFilter:
    email: str = Query('')

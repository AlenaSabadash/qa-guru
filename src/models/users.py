from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str

import json
from pathlib import Path
from typing import Sequence

from src.models.users import UserModel
from src.schemas.users import UserCreate, UserListResponse


def user_data():
    p = Path(__file__).with_name('users_data.json')
    with p.open('r') as file_data:
        return json.load(file_data)


def users_list() -> Sequence[UserModel]:
    return [UserModel(**user) for user in user_data()]


def get_user_by_id(user_id: int) -> UserModel | None:
    users = UserListResponse(items=user_data())
    for user in users.items:
        if user.id == user_id:
            return user
    return None


def create_user(email: str, first_name: str, last_name: str) -> UserCreate:
    return UserCreate(
        email=email,
        first_name=first_name,
        last_name=last_name,
    )

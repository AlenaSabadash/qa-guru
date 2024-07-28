import json

from src.models.users import UserModel
from src.schemas.users import UserListResponse, UserCreate
from pathlib import Path


def user_data():
    p = Path(__file__).with_name('users_data.json')
    with p.open('r') as file_data:
        return json.load(file_data)


def users_list() -> UserListResponse:
    return UserListResponse(**user_data())


def get_user_by_id(user_id: int) -> UserModel | None:
    for user in UserListResponse(**user_data()).data:
        if user.id == user_id:
            return user
    return None


def create_user(email: str, first_name: str, last_name: str) -> UserCreate:
    return UserCreate(
        email=email,
        first_name=first_name,
        last_name=last_name,
    )

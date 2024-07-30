import pytest
import requests
from fastapi import status

from src.models.users import UserModel
from src.schemas.users import UserCreate


def test_get_users_list(api_host):
    response = requests.get(f"{api_host}/api/users")
    users = response.json().get("data")
    for user in users:
        UserModel.model_validate(user)

    assert response.status_code == status.HTTP_200_OK
    assert len(users)


@pytest.mark.parametrize("user_id", list(range(1, 7)))
def test_get_specific_user(api_host, user_id):
    response = requests.get(f"{api_host}/api/users/{user_id}")
    user = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert user_id == user.get('id')


@pytest.mark.parametrize("user_id", list(range(666, 669)))
def test_get_specific_user_not_found(api_host, user_id):
    response = requests.get(f"{api_host}/api/users/{user_id}")
    user = response.json()

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert not user.get('id')
    assert user_id != user.get('id')


def test_create_new_user(api_host):
    new_user = UserCreate(
        email="example@mail.com",
        first_name="firstname",
        last_name="lastname",
    )

    response = requests.post(f"{api_host}/api/users", json=new_user.dict())
    user = UserCreate(**response.json())

    assert response.status_code == status.HTTP_200_OK
    assert new_user.email == user.email
    assert new_user.first_name == user.first_name
    assert new_user.last_name == user.last_name

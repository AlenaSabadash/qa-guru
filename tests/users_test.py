import json

import pytest
import requests
from fastapi import status
from random import randint

from src.dto.user import UserRead, BaseUser

host = 'http://127.0.0.1:8000'


@pytest.mark.usefixtures("fill_test_data")
def test_get_users_list(api_host):
    response = requests.get(f"{api_host}/api/v1/users/")
    users = response.json().get("items", [])
    for user in users:
        UserRead(**user)


def test_get_specific_user(api_host, fill_test_data):
    email = fill_test_data[0]["email"]
    response = requests.get(f"{api_host}/api/v1/users/?email={email}")
    users = response.json().get("items", [])

    assert response.status_code == status.HTTP_200_OK
    assert len(users)
    assert email == users[0].get('email')


@pytest.mark.parametrize("email", ["user@example666.com"])
def test_get_specific_user_not_found(api_host, email):
    response = requests.get(f"{api_host}/api/v1/users/?email={email}")
    users = response.json().get("items", [])

    assert response.status_code == status.HTTP_200_OK
    assert not len(users)


def test_create_new_user(api_host, fill_test_data):
    new_user = BaseUser(**fill_test_data[0])

    response = requests.post(f"{api_host}/api/v1/users/", json=new_user.dict())
    user = BaseUser(**response.json())

    assert response.status_code == status.HTTP_201_CREATED
    assert new_user.email == user.email
    assert new_user.first_name == user.first_name
    assert new_user.last_name == user.last_name

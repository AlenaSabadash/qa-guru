from fastapi import status
from random import randint

import requests

host = 'http://127.0.0.1:8000'


def test_get_users_list():
    response = requests.get(f"{host}/api/users")
    body = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert len(body.get("data", []))


def test_get_specific_user():
    user_id = randint(1, 6)
    response = requests.get(f"{host}/api/users/{user_id}")
    user = response.json()

    assert user_id == user.get('id')


def test_get_specific_user_not_found():
    user_id = 666
    response = requests.get(f"{host}/api/users/{user_id}")
    user = response.json()

    assert not user.get('id')
    assert user_id != user.get('id')


def test_create_new_user():
    new_user_data = {
      "email": "example@mail.com",
      "first_name": "firstname",
      "last_name": "lastname",
    }

    response = requests.post(f"{host}/api/users", json=new_user_data)
    user = response.json()

    assert new_user_data["email"] == user.get("email")
    assert new_user_data["first_name"] == user.get("first_name")
    assert new_user_data["last_name"] == user.get("last_name")

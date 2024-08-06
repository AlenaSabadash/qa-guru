import json
import os

import dotenv
import pytest
import requests


@pytest.fixture(scope="session", autouse=True)
def envs():
    dotenv.load_dotenv()


@pytest.fixture(scope="session")
def api_host():
    return f"http://{os.getenv('HOST')}:{os.getenv('BACKEND_PORT')}"


@pytest.fixture(scope="module")
def fill_test_data(api_host):
    with open("../users.json") as f:
        test_data_users = json.load(f)
    api_users = []
    for user in test_data_users:
        response = requests.post(f"{api_host}/api/v1/users/", json=user)
        api_users.append(response.json())

    user_ids = [user["id"] for user in api_users]

    yield api_users

    for user_id in user_ids:
        requests.delete(f"{api_host}/api/v1/users/{user_id}")

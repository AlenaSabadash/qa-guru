import os

import dotenv
import pytest


@pytest.fixture(autouse=True)
def envs():
    dotenv.load_dotenv()


@pytest.fixture()
def api_host():
    return os.getenv('API_HOST')

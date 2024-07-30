import pytest
import requests
from starlette import status


@pytest.mark.smoke
def test_healthcheck(api_host):
    response = requests.get(f"{api_host}/status")
    health = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert health == "pong"

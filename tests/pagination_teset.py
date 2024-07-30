import pytest
import requests
from starlette import status

TOTAL_SIZE = 6


@pytest.mark.parametrize("page,size", [(1, 1), (1, 2), (2, 2)])
def test_users_pagination(api_host, page, size):
    response = requests.get(f"{api_host}/api/users?page={page}&size={size}")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.parametrize("page,size", [(1, 1), (1, 2), (2, 2)])
def test_users_pagination_total(api_host, page, size):
    response = requests.get(f"{api_host}/api/users?page={page}&size={size}")
    assert response.json()["total"] == TOTAL_SIZE


@pytest.mark.parametrize("page,size", [(1, 1), (1, 2), (2, 2)])
def test_users_pagination_size(api_host, page, size):
    response = requests.get(f"{api_host}/api/users?page={page}&size={size}")
    assert response.json()["size"] == size


@pytest.mark.parametrize("page,size", [(1, 1), (1, 2), (2, 2)])
def test_users_pagination_size(api_host, page, size):
    response = requests.get(f"{api_host}/api/users?page={page}&size={size}")
    assert response.json()["page"] == page


@pytest.mark.parametrize("page,size,pages", [(1, 1, 6), (1, 2, 3), (1, 4, 2)])
def test_users_pagination_pages(api_host, page, size, pages):
    response = requests.get(f"{api_host}/api/users?page={page}&size={size}")
    assert response.json()["pages"] == pages

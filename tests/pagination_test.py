import pytest
import requests
from starlette import status

from src.schemas.users import UserListResponse

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


@pytest.mark.parametrize("pages,size", [([1, 2], 1)])
def test_users_data_is_different_on_page_change(api_host, pages, size):
    current_page, next_page = pages
    first_page_response = requests.get(f"{api_host}/api/users?page={current_page}&size={size}")
    next_page_response = requests.get(f"{api_host}/api/users?page={next_page}&size={size}")

    first_page_users = UserListResponse(**first_page_response.json()).items
    next_page_users = UserListResponse(**next_page_response.json()).items

    assert len(first_page_users) == size
    assert len(next_page_users) == size
    assert first_page_users[0].id != next_page_users[0].id
    assert first_page_users[0].email != next_page_users[0].email

import pytest
import requests
from starlette import status


@pytest.mark.parametrize("page,size", [(1, 1), (1, 2), (2, 2)])
@pytest.mark.usefixtures("fill_test_data")
def test_users_pagination(api_host, page, size):
    response = requests.get(f"{api_host}/api/v1/users/?page={page}&size={size}")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.parametrize("page,size", [(1, 1), (1, 2), (2, 2)])
@pytest.mark.usefixtures("fill_test_data")
def test_users_pagination_size(api_host, page, size):
    response = requests.get(f"{api_host}/api/v1/users/?page={page}&size={size}")
    assert response.json()["size"] == size


@pytest.mark.parametrize("page,size", [(1, 1), (1, 2), (2, 2)])
@pytest.mark.usefixtures("fill_test_data")
def test_users_pagination_size(api_host, page, size):
    response = requests.get(f"{api_host}/api/v1/users/?page={page}&size={size}")
    assert response.json()["page"] == page


@pytest.mark.parametrize("pages,size", [([1, 2], 1)])
@pytest.mark.usefixtures("fill_test_data")
def test_users_data_is_different_on_page_change(api_host, pages, size):
    current_page, next_page = pages
    first_page_response = requests.get(f"{api_host}/api/v1/users/?page={current_page}&size={size}")
    next_page_response = requests.get(f"{api_host}/api/v1/users/?page={next_page}&size={size}")

    first_page_users = first_page_response.json()["items"]
    next_page_users = next_page_response.json()["items"]

    assert len(first_page_users) == size
    assert len(next_page_users) == size
    assert first_page_users[0]["id"] != next_page_users[0]["id"]


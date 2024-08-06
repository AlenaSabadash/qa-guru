from typing import Any

from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params, paginate
from starlette import status

from src.dto.user import UserRead, UserFilter, BaseUser
from src.entity.user import User
from src.services.users_service import UserService
from src.usecase.utils import response
from src.usecase.utils.responses import SuccessfulResponse

router = APIRouter()


@router.get('/', response_model=Page[UserRead])
async def read_users(
    dto: UserFilter = Depends(),
    pagination_params: Params = Depends(),
    user_service: UserService = Depends(),
) -> Any:
    users = await user_service.find(dto)
    return paginate(users, pagination_params)


@router.post(
    path='/',
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    dto: BaseUser,
    user_service: UserService = Depends(),
) -> User:
    return await user_service.create(dto)


@router.delete(
    path='/{user_id}',
    responses=response.HTTP_404_NOT_FOUND(
        'User not found',
    ) | SuccessfulResponse.schema(),
)
async def delete_user(
    user_id: int,
    user_service: UserService = Depends(),
) -> SuccessfulResponse:
    await user_service.delete(user_id)
    return SuccessfulResponse()

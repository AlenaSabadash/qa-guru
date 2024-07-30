from typing import Any

from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params, paginate

from src.models.users import UserModel
from src.schemas.users import UserCreate, UserResponse
from src.services.users_service import (create_user_service, get_user_by_id,
                                        get_users_service)

router = APIRouter()


@router.get("/api/users", response_model=Page[UserModel])
async def get_users(pagination_params: Params = Depends()) -> Any:
    """
    Возвращает список пользоваителей
    """
    return paginate(await get_users_service(), pagination_params)


@router.get("/api/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int) -> UserModel:
    """
    Возвращает пользователя по id
    """
    return await get_user_by_id(user_id)


@router.post("/api/users", response_model=UserCreate)
async def create_user(user: UserCreate) -> UserCreate:
    """
    Создаем нового пользователя
    """
    return await create_user_service(user)

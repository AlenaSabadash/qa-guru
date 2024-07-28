from fastapi import APIRouter

from src.models.users import UserModel
from src.schemas.users import UserResponse, UserListResponse, UserCreate
from src.services.users_service import get_users_service, get_user_by_id, create_user_service

router = APIRouter()


@router.get("/api/users", response_model=UserListResponse)
async def get_users() -> UserListResponse:
    """
    Возвращает список пользоваителей
    """
    return await get_users_service()


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

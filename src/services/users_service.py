from fastapi import HTTPException, status

from src.models.users import UserModel
from src.repositories import users_repo
from src.schemas.users import UserListResponse, UserCreate


async def get_users_service() -> UserListResponse:
    return users_repo.users_list()


async def get_user_by_id(user_id: int) -> UserModel | HTTPException:
    user = users_repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found',
        )
    return user


async def create_user_service(user: UserCreate) -> UserCreate:
    return UserCreate(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
    )

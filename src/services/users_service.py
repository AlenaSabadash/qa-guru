from typing import Sequence

import sqlalchemy as sa
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.database import context_session
from src.dto.user import UserFilter, BaseUser
from src.entity.user import User
from src.repositories.repository import InjectRepository


class UserService:

    def __init__(
        self, session: AsyncSession = Depends(context_session),
    ) -> None:
        self.repository = InjectRepository(User, session)

    async def create(self, dto: BaseUser) -> User:
        user = self.repository.create(**dto.dict())
        return await self.repository.save(user)

    async def find(self, dto: UserFilter) -> Sequence[User]:
        return await self.repository.find(
            User.deleted_at.is_(None),
            User.email.contains(dto.email),
        )

    async def find_one_or_fail(self, user_id: int) -> User:
        return await self.repository.find_one_or_fail(
            User.deleted_at.is_(None), id=user_id,
        )

    async def delete(self, user_id: int) -> User:
        user = await self.find_one_or_fail(user_id)
        self.repository.merge(user, deleted_at=sa.func.now())
        return await self.repository.save(user)

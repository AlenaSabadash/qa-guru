from fastapi import APIRouter

from . import users, health

router = APIRouter()
router.include_router(
    users.router,
    prefix='/users',
    tags=['users'],
)
router.include_router(
    health.router,
    prefix='/status',
    tags=['health'],
)

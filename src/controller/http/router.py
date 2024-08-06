from fastapi import APIRouter

from src.controller.http import v1

api_router = APIRouter()
api_router.include_router(v1.router, prefix='/api/v1')

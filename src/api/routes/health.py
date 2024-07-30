from fastapi import APIRouter
from starlette import status

router = APIRouter()


@router.get("/status", status_code=status.HTTP_200_OK)
async def healthcheck() -> str:
    """
    Мониторинг работоспособности сервиса
    """
    return "pong"

from typing import Any, Dict, List

from environs import Env
from pydantic import (
    AnyHttpUrl,
    BaseSettings,
    PostgresDsn,
    validator,
)

env = Env()
env.read_env()


class Settings(BaseSettings):

    API: str = '/controller'
    DOCS: str = '/docs'
    STARTUP: str = 'startup'
    SHUTDOWN: str = 'shutdown'

    NAME: str = 'FastAPI QA-Guru API'
    VERSION: str = '1.0'
    DESCRIPTION: str = 'FastAPI QA-Guru'

    SWAGGER_UI_PARAMETERS: Dict[str, Any] = {
        'displayRequestDuration': True,
        'filter': True,
    }

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(
        cls, value: str | List[str],  # noqa: N805, WPS110
    ) -> str | List[str]:
        if isinstance(value, str) and not value.startswith('['):
            return [i.strip() for i in value.split(',')]
        elif isinstance(value, (list, str)):
            return value

        raise ValueError(value)

    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DATABASE_URI: PostgresDsn = (
        f"postgresql+asyncpg://"
        f"{env('DB_USER')}:{env('DB_PASSWORD')}@"
        f"{env('DB_HOST')}:{env('DB_PORT')}/"
        f"{env('DB_NAME')}"
    )

    @validator('DATABASE_URI', pre=True)
    def assemble_db_connection(
        cls, value: str | None,  # noqa: N805, WPS110
    ) -> str:
        if isinstance(value, str):
            return value

        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            user=env.str('DB_USER'),
            password=env.str('DB_PASSWORD'),
            host=env.str('DB_HOST'),
            port=env.str('DB_PORT'),
            path='/{0}'.format(env.str('DB_NAME')),
        )

    class Config(object):
        case_sensitive = True


settings = Settings()

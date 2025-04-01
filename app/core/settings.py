"""App settings."""

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    app_title: str = 'Bet Marker'
    postgres_user: str = 'postgres'
    postgres_password: str = 'postgres'
    postgres_db: str = 'postgres'
    postgres_dsn: PostgresDsn = 'postgresql+asyncpg://postgres:postgres@postgres:5432/postgres'

    class Config:
        env_file = '.env'


settings = BaseConfig()

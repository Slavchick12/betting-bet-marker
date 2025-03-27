"""App settings."""

from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    app_title: str = 'Bet Marker'
    postgres_user: str = 'postgres'
    postgres_password: str = 'postgres'
    postgres_db: str = 'postgres'

    class Config:
        env_file = '.env'


settings = BaseConfig()

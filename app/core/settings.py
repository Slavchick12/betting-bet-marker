"""App settings."""

from pydantic_settings import BaseSettings
from pydantic import PostgresDsn


class BaseConfig(BaseSettings):
    app_title: str = 'Bet Marker'
    postgres_user: str = 'postgres'
    postgres_password: str = 'postgres'
    postgres_db: str = 'postgres'
    postgres_dsn: PostgresDsn = 'postgres'
    line_provider_service_name: str = 'line-provider'
    line_provider_service_port: int = 8001

    class Config:
        env_file = '.env'


settings = BaseConfig()

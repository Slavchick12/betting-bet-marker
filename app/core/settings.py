"""App settings."""

from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    app_title: str = 'Bet Marker'

    class Config:
        env_file = '.env'


settings = BaseConfig()

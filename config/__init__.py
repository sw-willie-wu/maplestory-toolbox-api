from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

from .db import PostgresSetting


class Settings(BaseSettings):
    Name: str = 'Maplestory Toolbox Api'
    Mode: Literal['DEV', 'PROD'] = 'DEV'
    Postgres: PostgresSetting = PostgresSetting()

    model_config = SettingsConfigDict(
        env_prefix='APP_',
        env_nested_delimiter='__'
    )


def get_settings() -> Settings:
    return Settings()


SETTINGS = get_settings()

from functools import lru_cache
from typing import Annotated

from pydantic import field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "Test Backend"
    app_version: str = "0.1.0"

    mysql_user: str
    mysql_password: str
    mysql_host: str
    mysql_port: int
    mysql_database: str

    cors_allowed_origins: Annotated[list[str], NoDecode] = []
    cors_allowed_methods: Annotated[list[str], NoDecode] = ["*"]
    cors_allowed_headers: Annotated[list[str], NoDecode] = ["*"]
    cors_allow_credentials: bool = True

    @field_validator(
        "cors_allowed_origins",
        "cors_allowed_methods",
        "cors_allowed_headers",
        mode="before",
    )
    @classmethod
    def _split_csv(cls, value):
        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        return value


@lru_cache
def get_settings() -> Settings:
    return Settings()

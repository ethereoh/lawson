from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

import torch


class AppSettings(BaseModel):
    TITLE: str = "Lawson AI"
    PLACEHOLDER: str = "temp"
    VERSION: str = "0.0.0"
    DEVICE: str = "cuda" if torch.cuda.is_available() else "cpu"


class Settings(BaseSettings):
    """
    Settings for the application.
    All settings here are easily changed by the change of .env variables
    """

    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )

    VECTORDB_HOST: str
    VECTORDB_PORT: int

    APP_HOST: str
    APP_PORT: int
    ENVIRONMENT: str  # dev or prod

    # ===== OTHERS =====
    LOGGER: str


settings = Settings()
app_settings = AppSettings()

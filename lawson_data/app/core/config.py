from pydantic import BaseModel 
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseModel): 
    TITLE: str = "Lawson Data Handler"
    PLACEHOLDER: str = "temp"
    VERSION: str = "0.0.0"

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
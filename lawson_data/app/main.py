from fastapi import FastAPI
from pathlib import Path
from contextlib import asynccontextmanager

from app.api import data_loader
from app.core.config import app_settings, settings
from app.common.logging_config import setup_logger

logger = setup_logger(settings.LOGGER)

@asynccontextmanager
async def lifespan(app: FastAPI):
    PLACEHOLDER = Path(app_settings.PLACEHOLDER)
    PLACEHOLDER.mkdir(exist_ok=True)
    logger.info("Welcome to server")
    yield
    logger.warning("Shutting down the server")

app = FastAPI(
  title=app_settings.TITLE,
  docs_url="/docs",
  lifespan=lifespan,
  version=app_settings.VERSION,
)


app.include_router(data_loader.router, prefix="")

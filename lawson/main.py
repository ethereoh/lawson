from fastapi import FastAPI
from pathlib import Path
from contextlib import asynccontextmanager

from lawson.api import data_loader
from lawson.core.config import app_settings, settings
from lawson.common.logging_config import setup_logger

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


@app.get("/")
async def hello_word():
    return {"msg": "hello world"}


app.include_router(data_loader.router, prefix="")

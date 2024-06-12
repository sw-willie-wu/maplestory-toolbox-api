import logging
from typing import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import DATABASE
from config import SETTINGS
from router import api_router



LOGGER = logging.getLogger(__name__)

async def startup() -> None:
    LOGGER.info("APP initializing...")
    # await DATABASE.migrate()


async def shutdown() -> None:
    LOGGER.info("APP shutdown...")

    await DATABASE.close()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator:
    await startup()
    yield
    await shutdown()


app = FastAPI(
    version="0.1",
    debug=True if SETTINGS.Mode == 'DEV' else False,
    title=SETTINGS.Name,
    lifespan=lifespan,
    docs_url="/docs",
    openapi_url="/openapi.json",
)

origins = ["maplestory-toolbox.vercel.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    api_router
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# import secrets
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
# security = HTTPBasic()
# def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
#     correct_username = secrets.compare_digest(credentials.username, "user")
#     correct_password = secrets.compare_digest(credentials.password, "password")
#     if not (correct_username and correct_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect email or password",
#             headers={"WWW-Authenticate": "Basic"},
#         )
#     return credentials.username
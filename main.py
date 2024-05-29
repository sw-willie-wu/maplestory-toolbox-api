from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import api_router

app = FastAPI(
    version="0.1",
    debug=False,
    title='maplestory-toolbox-api',
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(RequestHandlingMiddleware)

app.include_router(
    api_router,
    prefix="/api"
)


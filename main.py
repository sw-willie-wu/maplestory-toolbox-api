from fastapi import FastAPI

from router import api_router


app = FastAPI(
    version="0.1",
    debug=False,
    title="maplestory-toolbox-api",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.include_router(
    api_router,
    prefix="/api"
)



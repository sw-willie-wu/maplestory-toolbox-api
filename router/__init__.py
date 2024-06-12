from fastapi import APIRouter, Depends
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html

from service import Validator
from router.icon import icon_router
from router.rune import rune_router


api_router = APIRouter()

api_router.include_router(
    icon_router,
    prefix="/icon",
    tags=["Icon"],
)

api_router.include_router(
    rune_router,
    prefix="/rune",
    tags=["Rune"],
)

# @api_router.get("/docs", include_in_schema=False)
# async def docs(user: str = Depends(Validator.valid_admin)):
#     return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

# @api_router.get("/openapi.json", include_in_schema=False)
# async def openapi(user: str = Depends(Validator.valid_admin)):
#     return get_openapi(title = "FastAPI", version="0.1.0", routes=api_router.routes)

# @api_router.get(
#     "/crawl",
#     status_code=status.HTTP_200_OK,
#     # response_model=GridRawDataResponse
# )
# def crawl(request: Request, event_name: str):

#     return crawl_img(event_name)


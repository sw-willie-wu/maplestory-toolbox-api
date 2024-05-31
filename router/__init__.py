from starlette import status
from fastapi import APIRouter, Request

from service import crawl_img
# from .middleware import RequestHandlingMiddleware


api_router = APIRouter()


@api_router.get(
    "/crawl",
    status_code=status.HTTP_200_OK,
    # response_model=GridRawDataResponse
)
def crawl(request: Request, event_name: str):

    return crawl_img(event_name)


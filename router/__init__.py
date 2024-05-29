from starlette import status
from fastapi import APIRouter, Request

# from .middleware import RequestHandlingMiddleware


api_router = APIRouter()


@api_router.get(
    "/test",
    status_code=status.HTTP_200_OK,
    # response_model=GridRawDataResponse
)
def test(request: Request):

    return dict(data=123)


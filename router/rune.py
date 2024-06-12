from starlette import status
from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from db import DATABASE
from service.rune import RuneWriter, RuneReader
from schema.base import BaseResponse
from schema.rune import Rune as RuneSchema



rune_router = APIRouter()


@rune_router.get(
    "/list",
    status_code=status.HTTP_200_OK,
    response_description="資料查詢成功",
    response_model=BaseResponse,
)
async def list_all(
    request: Request, 
    offset: int = 0,
    limit: int = -1,
    db_session: AsyncSession = Depends(DATABASE.get_session)
):
    reader = RuneReader(db_session)
    result = await reader.load_all(offset, limit)

    return BaseResponse(
        StatusCode=status.HTTP_200_OK,
        Description='資料查詢成功',
        Data=result
    )
#     return FileResponse(f'icon/{id}.png', media_type="image/png")


@rune_router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_description="資料建立成功",
    response_model=BaseResponse,
)
async def create_rune(
    rune: RuneSchema,
    request: Request, 
    db_session: AsyncSession = Depends(DATABASE.get_session)
):
    writer = RuneWriter(db_session)
    result = await writer.save_data_from_schema(rune)

    await db_session.commit()

    return BaseResponse(
        StatusCode=status.HTTP_201_CREATED,
        Description="資料建立成功",
        Data=result,
    )

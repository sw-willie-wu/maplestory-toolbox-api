from fastapi import APIRouter, Request
from fastapi.responses import FileResponse


icon_router = APIRouter()


@icon_router.get("/{id}", response_class=FileResponse)
async def icon(request: Request, id: int):
    return FileResponse(f'icon/{id}.png', media_type="image/png")

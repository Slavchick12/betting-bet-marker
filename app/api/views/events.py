"""Views for events routers."""

from fastapi import APIRouter, status
from app.utils.constants import LINE_PROVIDER_URL

import httpx

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK, response_model=list)
async def list_event() -> list:
    async with httpx.AsyncClient() as client:
        response = await client.get(LINE_PROVIDER_URL + '/api/v1/events/')
    return response.json()

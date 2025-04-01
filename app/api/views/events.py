"""Views for events routers."""

from uuid import UUID

import httpx
from fastapi import APIRouter, status

from app.api.services.bets import BetService
from app.db.schemas import StatusUpdateSchema
from app.utils.constants import LINE_PROVIDER_URL

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK, response_model=list)
async def list_event() -> list:
    async with httpx.AsyncClient() as client:
        response = await client.get(LINE_PROVIDER_URL + '/api/v1/events/')
    return response.json()


@router.patch('/{uuid}/status', status_code=status.HTTP_204_NO_CONTENT)
async def update_status(uuid: UUID, status_schema: StatusUpdateSchema) -> None:
    """Callback url for change event status."""
    return await BetService.update_status(event_uuid=uuid, event_status=status_schema.event_status)

"""Views for bet routers."""

import httpx
from fastapi import APIRouter, HTTPException, status

from app.api.services.bets import BetService
from app.db.schemas import BetCreateSchema, BetListSchema, BetSchema
from app.utils.constants import LINE_PROVIDER_URL

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[BetListSchema])
async def bets_list() -> list[BetListSchema]:
    return await BetService.list()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=BetSchema)
async def bets_create(bet: BetCreateSchema) -> BetSchema:
    async with httpx.AsyncClient() as client:
        events_json = (await client.get(LINE_PROVIDER_URL + '/api/v1/events/')).json()  # TODO: improve by caching
        if (event_uuid := str(bet.event_uuid)) not in [event['uuid'] for event in events_json]:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Event with uuid {event_uuid} not found')

    return await BetService.create(bet)


# докерфайл настроить  запуск миграций alembic upgrade head
# README
# настроить обновление статуса ставки
# response model везде и типизацию в прицнипе

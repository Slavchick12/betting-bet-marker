from uuid import UUID

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, update

from app.db.connetion import get_session
from app.db.models import Bet
from app.db.schemas import BetCreateSchema
from app.utils.enums import EventStatusEnum


class BetService:
    @classmethod
    async def list(cls):
        statement = select(Bet)
        async with get_session() as db:
            results = await db.execute(statement=statement)
        return results.scalars().all()

    @classmethod
    async def create(cls, bet_in: BetCreateSchema) -> Bet:
        bet_in_json = jsonable_encoder(bet_in)
        bet_obj = Bet(**bet_in_json)

        async with get_session() as db:
            db.add(bet_obj)
            await db.commit()

        return bet_obj

    @classmethod
    async def update_status(cls, event_uuid: UUID, event_status: EventStatusEnum):
        statement = update(Bet).where(Bet.event_uuid == event_uuid).values(event_status=event_status)
        async with get_session() as db:
            await db.execute(statement=statement)
            await db.commit()

from typing import Annotated
from uuid import UUID

from fastapi import HTTPException, status
from pydantic import BaseModel, Field, field_validator

from app.utils.enums import EventStatusEnum


class BetSchema(BaseModel):
    uuid: UUID
    event_uuid: UUID
    amount: Annotated[float, Field(gt=0)]
    event_status: EventStatusEnum


class BetCreateSchema(BaseModel):
    event_uuid: UUID
    amount: Annotated[float, Field(gt=0)]

    @field_validator('amount')
    @classmethod
    def amount_validate(cls, amount: float) -> float:
        if round(amount, 2) != amount:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='Amount can contain up to 2 decimal places',
            )
        return amount


class BetListSchema(BaseModel):
    event_uuid: UUID
    event_status: EventStatusEnum


class StatusUpdateSchema(BaseModel):
    event_status: EventStatusEnum

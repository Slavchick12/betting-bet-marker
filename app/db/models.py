"""Models for database tables."""

import uuid as uuid_lib

from sqlalchemy import Column, String, Enum, UUID
from sqlalchemy.orm import declarative_base
from app.utils.enums import BetStatusEnum

Base = declarative_base()


class Bet(Base):
    __tablename__ = 'bet'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid_lib.uuid4)
    event_uuid = Column(UUID(as_uuid=True), default=uuid_lib.uuid4)
    amount = Column(String(100))
    status = Column(Enum(BetStatusEnum), nullable=False, default=BetStatusEnum.in_progress)

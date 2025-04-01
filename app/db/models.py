"""Models for database tables."""

import uuid as uuid_lib

from sqlalchemy import FLOAT, UUID, CheckConstraint, Column, Enum
from sqlalchemy.orm import declarative_base, validates

from app.utils.enums import EventStatusEnum

Base = declarative_base()


class Bet(Base):
    __tablename__ = 'bet'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid_lib.uuid4)
    amount = Column(FLOAT(), nullable=False)
    event_uuid = Column(UUID(as_uuid=True), nullable=False)
    event_status = Column(Enum(EventStatusEnum), nullable=False, default=EventStatusEnum.in_progress)

    __table_args__ = (
        CheckConstraint(amount > 0, name='positive_amount'),
    )

    @validates('amount')
    def validate_amount(self, key, amount):
        if round(amount, 2) != amount:
            raise ValueError('Amount can contain up to 2 decimal places.')
        return amount

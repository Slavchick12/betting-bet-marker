"""Enums."""

from enum import Enum


class EventStatusEnum(str, Enum):
    in_progress = 'In progress'
    win = 'Win'
    loss = 'Loss'

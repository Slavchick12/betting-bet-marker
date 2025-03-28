"""Enums."""

from enum import Enum


class BetStatusEnum(str, Enum):
    in_progress = 'In progress'
    win = 'Win'
    loss = 'Loss'

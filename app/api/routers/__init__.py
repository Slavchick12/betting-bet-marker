"""Main routers."""

from fastapi import APIRouter

from .bets import router as bets_router
from .events import router as events_router

router = APIRouter()

router.include_router(bets_router, prefix='/bets')
router.include_router(events_router, prefix='/events')

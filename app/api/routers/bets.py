"""Api urls for bets."""

from fastapi import APIRouter

from app.api.views.bets import router as bets

router = APIRouter(tags=['bets'])

router.include_router(bets)

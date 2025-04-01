"""Connection to database."""

from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.settings import settings

engine = create_async_engine(str(settings.postgres_dsn), echo=True, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@asynccontextmanager
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

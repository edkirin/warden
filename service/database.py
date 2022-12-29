import logging
from typing import AsyncIterator, Type

from sqlalchemy.engine import URL
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from service.config import settings

logger = logging.getLogger(__name__)

db_connect_url = URL.create(
    drivername="postgresql+asyncpg",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)

async_engine = create_async_engine(url=db_connect_url)

AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    autoflush=False,
    future=True,
    class_=AsyncSession,
)


async def get_session() -> AsyncIterator[sessionmaker]:
    try:
        yield AsyncSessionLocal
    except SQLAlchemyError as e:
        logger.exception(e)

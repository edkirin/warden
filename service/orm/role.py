from __future__ import annotations

from typing import AsyncIterator
from sqlalchemy import Column, Integer, String, select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .base import Base


class RoleModel(Base):
    __tablename__ = "roles"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)

    @classmethod
    async def read_all(cls, session: AsyncSession) -> AsyncIterator[RoleModel]:
        stmt = select(cls).options(selectinload(cls.feature_group))
        stream = await session.stream(stmt.order_by(cls.id))
        async for row in stream:
            yield row.RoleModel

    @classmethod
    async def delete_all(cls, session: AsyncSession) -> None:
        stmt = delete(cls)
        await session.execute(stmt)
        await session.commit()

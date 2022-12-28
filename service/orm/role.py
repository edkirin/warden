from __future__ import annotations

from typing import AsyncIterator, Optional

from sqlalchemy import Column, Integer, String, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .base import Base


class RoleModel(Base):
    __tablename__ = "roles"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)

    @classmethod
    async def get_by_id(
        cls, session: AsyncSession, role_id: int
    ) -> Optional[RoleModel]:
        query = select(cls).where(cls.id == role_id)
        result = (await session.execute(query)).first()
        return result.RoleModel if result else None

    @classmethod
    async def read_all(cls, session: AsyncSession) -> AsyncIterator[RoleModel]:
        query = select(cls).options(selectinload(cls.feature_group))
        stream = await session.stream(query.order_by(cls.id))
        async for row in stream:
            yield row.RoleModel

    @classmethod
    async def delete_all(cls, session: AsyncSession) -> None:
        query = delete(cls)
        await session.execute(query)
        await session.commit()

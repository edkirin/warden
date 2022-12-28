from __future__ import annotations

from dataclasses import dataclass
from typing import AsyncIterator
from sqlalchemy import Table, Column, Integer, String, select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .base import mapper_registry


@mapper_registry.mapped
@dataclass
class RoleModel:
    __table__ = Table(
        "roles",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
    )

    id: int
    name: str

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

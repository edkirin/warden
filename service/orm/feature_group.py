from __future__ import annotations

from dataclasses import field, dataclass
from typing import AsyncIterator
from sqlalchemy import Table, Column, Integer, String, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
@dataclass
class FeatureGroupModel:
    __table__ = Table(
        "feature_groups",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
        Column("field_name", String),
    )

    id: int = field(init=False)
    name: str
    field_name: str

    @classmethod
    async def read_all(cls, session: AsyncSession) -> AsyncIterator[FeatureGroupModel]:
        stmt = select(cls)
        stream = await session.stream(stmt.order_by(cls.id))
        async for row in stream:
            yield row.FeatureGroupModel

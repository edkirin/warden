from __future__ import annotations

from dataclasses import field, dataclass
from typing import AsyncIterator, Optional
from sqlalchemy import Table, Column, Integer, String, ForeignKey, select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship, selectinload

from .base import mapper_registry

from .feature_group import FeatureGroupModel


@mapper_registry.mapped
@dataclass
class FeatureModel:
    __table__ = Table(
        "features",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
        Column("field_name", String),
        Column("feature_group_id", Integer, ForeignKey("feature_groups.id")),
    )

    id: int
    name: str
    field_name: str
    feature_group: FeatureGroupModel

    __mapper_args__ = {
        "properties": {
            "feature_group": relationship(FeatureGroupModel),
        },
    }

    @classmethod
    async def read_all(
        cls, session: AsyncSession, feature_group_id: Optional[int] = None
    ) -> AsyncIterator[FeatureModel]:
        stmt = select(cls).options(selectinload(cls.feature_group))

        if feature_group_id is not None:
            stmt = stmt.where(cls.feature_group_id == feature_group_id)

        stream = await session.stream(stmt.order_by(cls.id))
        async for row in stream:
            yield row.FeatureModel

    @classmethod
    async def delete_all(cls, session: AsyncSession) -> None:
        stmt = delete(cls)
        await session.execute(stmt)
        await session.commit()

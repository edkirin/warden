from __future__ import annotations

from dataclasses import field, dataclass
from typing import AsyncIterator
from sqlalchemy import Table, Column, Integer, String, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship

from .base import mapper_registry

# from .feature import FeatureModel


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

    # id: int = field(init=False)
    id: int
    name: str
    field_name: str
    # features: list[FeatureModel]

    # __mapper_args__ = {  # type ignore
    #     "properties": {
    #         "features": relationship(FeatureModel, back_populates="feature_groups"),
    #     },
    # }

    @classmethod
    async def read_all(cls, session: AsyncSession) -> AsyncIterator[FeatureGroupModel]:
        stmt = select(cls)
        stream = await session.stream(stmt.order_by(cls.id))
        async for row in stream:
            yield row.FeatureGroupModel

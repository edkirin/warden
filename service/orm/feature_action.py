from __future__ import annotations

from dataclasses import dataclass
from typing import AsyncIterator
from sqlalchemy import Table, Column, Integer, String, select, delete, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, relationship

from . import FeatureModel
from .base import mapper_registry
from ..api.enums import ActionEnum


@mapper_registry.mapped
@dataclass
class FeatureActionModel:
    __table__ = Table(
        "feature_actions",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("feature_id", Integer, ForeignKey("features.id")),
        Column("action", String),
    )

    id: int
    feature: FeatureModel
    action: ActionEnum

    __mapper_args__ = {
        "properties": {
            "feature": relationship(FeatureModel),
        },
    }

    @classmethod
    async def read_all(cls, session: AsyncSession) -> AsyncIterator[FeatureActionModel]:
        stmt = select(cls).options(selectinload(cls.feature_group))
        stream = await session.stream(stmt.order_by(cls.id))
        async for row in stream:
            yield row.FeatureActionModel

    @classmethod
    async def delete_all(cls, session: AsyncSession) -> None:
        stmt = delete(cls)
        await session.execute(stmt)
        await session.commit()

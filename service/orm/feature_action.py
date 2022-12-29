from __future__ import annotations

from typing import AsyncIterator
from sqlalchemy import Column, Integer, String, select, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, relationship

from . import FeatureModel
from .base import ModelBase
from service.api.enums import ActionEnum


class FeatureActionModel(ModelBase):
    __tablename__ = "feature_actions"

    id: int = Column(Integer, primary_key=True)
    feature_id: int = Column(Integer, ForeignKey("features.id"))
    action: ActionEnum = Column(String)
    feature: FeatureModel = relationship("FeatureModel", uselist=False)

    @classmethod
    async def read_all(cls, session: AsyncSession) -> AsyncIterator[FeatureActionModel]:
        stmt = select(cls).options(selectinload(cls.feature_group))
        stream = await session.stream(stmt.order_by(cls.id))
        async for row in stream:
            yield row.FeatureActionModel

from __future__ import annotations

from typing import AsyncIterator, Optional
from sqlalchemy import Column, Integer, String, ForeignKey, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship, joinedload

from .base import ModelBase


class FeatureModel(ModelBase):
    __tablename__ = "features"

    id: int = Column(Integer, primary_key=True)
    parent_id: Optional[int] = Column(Integer, ForeignKey("features.id"), nullable=True)
    name: str = Column(String)
    field_name: str = Column(String)

    parent: FeatureModel = relationship("FeatureModel", back_populates="children", uselist=False)
    children: FeatureModel = relationship("FeatureModel")

    @classmethod
    async def read_all(
        cls, session: AsyncSession, parent_id: Optional[int] = None
    ) -> AsyncIterator[FeatureModel]:
        query = (
            select(cls)
            .execution_options(populate_existing=True)
            .options(joinedload(cls.parent))
        )

        if parent_id is not None:
            query = query.where(cls.parent_id == parent_id)

        stream = await session.stream(query.order_by(cls.id))

        async for row in stream.unique():
            yield row.FeatureModel

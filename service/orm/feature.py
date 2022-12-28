from __future__ import annotations

from typing import AsyncIterator, Optional
from sqlalchemy import Column, Integer, String, ForeignKey, select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship, joinedload

from .base import Base


class FeatureModel(Base):
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
        stmt = (
            select(cls)
            .execution_options(populate_existing=True)
            .options(joinedload(cls.parent))
        )

        if parent_id is not None:
            stmt = stmt.where(cls.parent_id == parent_id)

        stream = await session.stream(stmt.order_by(cls.id))

        async for row in stream.unique():
            yield row.FeatureModel

    @classmethod
    async def delete_all(cls, session: AsyncSession) -> None:
        stmt = delete(cls)
        await session.execute(stmt)
        await session.commit()

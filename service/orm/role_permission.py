from __future__ import annotations

from typing import AsyncIterator, Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, relationship

from service.api.enums import ActionEnum

from . import FeatureModel, RoleModel
from .base import Base


class RolePermissionModel(Base):
    __tablename__ = "role_permissions"

    id: int = Column(Integer, primary_key=True)
    role_id: int = Column(Integer, ForeignKey("roles.id"))
    feature_id: int = Column(Integer, ForeignKey("features.id"))
    action: ActionEnum = Column(String)
    permitted: bool = Column(Boolean)

    role: RoleModel = relationship("RoleModel", uselist=False)
    feature: FeatureModel = relationship("FeatureModel", uselist=False)

    @classmethod
    async def read_all(
        cls, session: AsyncSession, parent_id: Optional[int] = None
    ) -> AsyncIterator[RolePermissionModel]:
        stmt = (
            select(cls)
            .execution_options(populate_existing=True)
            .options(joinedload(cls.parent))
        )

        if parent_id is not None:
            stmt = stmt.where(cls.parent_id == parent_id)

        stream = await session.stream(stmt.order_by(cls.id))

        async for row in stream.unique():
            yield row.RolePermissionModel

    @classmethod
    async def delete_all(cls, session: AsyncSession) -> None:
        stmt = delete(cls)
        await session.execute(stmt)
        await session.commit()

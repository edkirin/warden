from __future__ import annotations

from typing import AsyncIterator, Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, relationship

from service.api.enums import ActionEnum

from . import FeatureModel, RoleModel
from .base import ModelBase


class RolePermissionModel(ModelBase):
    __tablename__ = "role_permissions"

    id: int = Column(Integer, primary_key=True)
    role_id: int = Column(Integer, ForeignKey("roles.id"))
    feature_id: int = Column(Integer, ForeignKey("features.id"))
    action: ActionEnum = Column(String)
    permitted: bool = Column(Boolean)

    role: RoleModel = relationship("RoleModel", uselist=False)
    feature: FeatureModel = relationship("FeatureModel", uselist=False)

    @classmethod
    async def get_by_id(
        cls, session: AsyncSession, id_: int
    ) -> Optional[RolePermissionModel]:
        query = select(cls).where(cls.id == id_)
        result = (await session.execute(query)).first()
        return result.RolePermissionModel if result else None

    @classmethod
    async def read_for_role_id(
        cls, session: AsyncSession, role_id: int
    ) -> AsyncIterator[RolePermissionModel]:
        query = (
            select(cls)
            .execution_options(populate_existing=True)
            .options(joinedload(cls.feature))
            .where(cls.role_id == role_id)
        )
        stream = await session.stream(query.order_by(cls.id))
        async for row in stream:
            yield row.RolePermissionModel

    @classmethod
    async def read_all(cls, session: AsyncSession) -> AsyncIterator[RolePermissionModel]:
        query = select(cls)
        stream = await session.stream(query.order_by(cls.id))
        async for row in stream:
            yield row.RolePermissionModel

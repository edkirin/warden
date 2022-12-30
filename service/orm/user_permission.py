from __future__ import annotations

from typing import AsyncIterator, Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, relationship

from service.api.enums import ActionEnum

from . import FeatureModel, UserModel
from .base import ModelBase


class UserPermissionModel(ModelBase):
    __tablename__ = "user_permissions"

    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer, ForeignKey("users.id"))
    feature_id: int = Column(Integer, ForeignKey("features.id"))
    action: ActionEnum = Column(String)
    permitted: bool = Column(Boolean)

    user: UserModel = relationship("UserModel", uselist=False)
    feature: FeatureModel = relationship("FeatureModel", uselist=False)

    @classmethod
    async def read_for_user_id(
        cls, session: AsyncSession, user_id: int
    ) -> AsyncIterator[UserPermissionModel]:
        query = (
            select(cls)
            .execution_options(populate_existing=True)
            .options(joinedload(cls.feature))
            .where(cls.user_id == user_id)
        )
        stream = await session.stream(query.order_by(cls.id))
        async for row in stream:
            yield row.UserPermissionModel

    @classmethod
    async def read_all(
        cls, session: AsyncSession, parent_id: Optional[int] = None
    ) -> AsyncIterator[UserPermissionModel]:
        query = (
            select(cls)
            .execution_options(populate_existing=True)
            .options(joinedload(cls.parent))
        )

        if parent_id is not None:
            query = query.where(cls.parent_id == parent_id)

        stream = await session.stream(query.order_by(cls.id))

        async for row in stream:
            yield row.UserPermissionModel

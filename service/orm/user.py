from __future__ import annotations

from typing import AsyncIterator, Optional

from sqlalchemy import Column, ForeignKey, Integer, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship, selectinload

from .base import ModelBase
from .role import RoleModel


class UserModel(ModelBase):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    tenant_id: int = Column(Integer)
    user_id: int = Column(Integer)
    role_id: int = Column(Integer, ForeignKey("roles.id"))
    role: RoleModel = relationship("RoleModel", uselist=False)

    @classmethod
    async def get_by_user_id(
        cls, session: AsyncSession, tenant_id: int, user_id: int
    ) -> Optional[UserModel]:
        query = select(cls).where(cls.tenant_id == tenant_id, cls.user_id == user_id)
        result = (await session.execute(query)).first()
        return result.UserModel if result else None

    @classmethod
    async def read_all(cls, session: AsyncSession) -> AsyncIterator[UserModel]:
        query = select(cls).options(selectinload(cls.feature_group))
        stream = await session.stream(query.order_by(cls.id))
        async for row in stream:
            yield row.UserModel

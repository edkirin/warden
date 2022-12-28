from __future__ import annotations

from typing import AsyncIterator

from sqlalchemy import Column, ForeignKey, Integer, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship, selectinload

from .base import Base
from .role import RoleModel


class UserModel(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    tenant_id: int = Column(Integer)
    user_id: int = Column(Integer)
    role_id: int = Column(Integer, ForeignKey("roles.id"))
    role: RoleModel = relationship("RoleModel", uselist=False)

    @classmethod
    async def read_all(cls, session: AsyncSession) -> AsyncIterator[UserModel]:
        stmt = select(cls).options(selectinload(cls.feature_group))
        stream = await session.stream(stmt.order_by(cls.id))
        async for row in stream:
            yield row.UserModel

    @classmethod
    async def delete_all(cls, session: AsyncSession) -> None:
        stmt = delete(cls)
        await session.execute(stmt)
        await session.commit()

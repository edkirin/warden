from typing import List, Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session, Query

from service.orm.feature_group import FeatureGroupModel


class PermissionsManager:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_feature_groups(self) -> List[FeatureGroupModel]:
        stmt = select(FeatureGroupModel).order_by(FeatureGroupModel.id)

        async with self.session.begin() as session:
            queryset = await session.execute(stmt)

        return queryset

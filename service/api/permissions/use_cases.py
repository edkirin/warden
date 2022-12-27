from typing import AsyncIterator

from fastapi import Depends
from service.api.permissions.schema import FeatureGroupDTO
from service.database import AsyncSessionClass, get_session
from service.orm.feature_group import FeatureGroupModel


class ReadAllFeatureGroups:
    def __init__(self, session: AsyncSessionClass = Depends(get_session)) -> None:
        self.async_session = session

    async def execute(self) -> AsyncIterator[FeatureGroupDTO]:
        async with self.async_session() as session:
            async for feature_group in FeatureGroupModel.read_all(session):
                yield FeatureGroupDTO.from_orm(feature_group)

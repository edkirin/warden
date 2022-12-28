from typing import AsyncIterator

from fastapi import Depends
from service.api.permissions.schema import FeatureDTO, FeatureGroupDTO
from service.database import AsyncSessionClass, get_session
from service.orm.feature import FeatureModel
from service.orm.feature_group import FeatureGroupModel


class ReadAllFeatureGroups:
    def __init__(self, session: AsyncSessionClass = Depends(get_session)) -> None:
        self.async_session = session

    async def execute(self) -> AsyncIterator[FeatureGroupDTO]:
        async with self.async_session() as session:
            async for feature_group in FeatureGroupModel.read_all(session):
                yield FeatureGroupDTO.from_orm(feature_group)


class ReadFeatureGroupFeatures:
    def __init__(self, session: AsyncSessionClass = Depends(get_session)) -> None:
        self.async_session = session

    async def execute(self, feature_group_id: int) -> AsyncIterator[FeatureDTO]:
        async with self.async_session() as session:
            async for feature in FeatureModel.read_all(
                session, feature_group_id=feature_group_id
            ):
                yield FeatureDTO.from_orm(feature)

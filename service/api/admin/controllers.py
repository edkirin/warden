from typing import AsyncIterator

from service.api.common.controller_base import ControllerBase
from service.api.admin.schema import FeatureDTO, FeatureGroupDTO
from service.dto.models import RoleDTO
from service.orm.feature import FeatureModel
from service.orm.feature_group import FeatureGroupModel
from service.orm.role import RoleModel


class ReadAllFeatureGroups(ControllerBase):
    async def execute(self) -> AsyncIterator[FeatureGroupDTO]:
        async with self.async_session() as session:
            feature_groups = FeatureGroupModel.read_all(session)
            async for feature_group in feature_groups:
                yield FeatureGroupDTO.from_orm(feature_group)


class ReadFeatureGroupFeatures(ControllerBase):
    async def execute(self, feature_group_id: int) -> AsyncIterator[FeatureDTO]:
        async with self.async_session() as session:
            features = FeatureModel.read_all(session, feature_group_id=feature_group_id)
            async for feature in features:
                yield FeatureDTO.from_orm(feature)


class ReadRoles(ControllerBase):
    async def execute(self) -> AsyncIterator[FeatureGroupDTO]:
        async with self.async_session() as session:
            roles = RoleModel.read_all(session)
            async for roles in roles:
                yield RoleDTO.from_orm(roles)


class DeleteAllData(ControllerBase):
    async def execute(self) -> None:
        async with self.async_session() as session:
            await RoleModel.delete_all(session)
            await FeatureModel.delete_all(session)
            await FeatureGroupModel.delete_all(session)



class ReadUserPermissions(ControllerBase):
    async def execute(self, tenant_id: int, user_id: int) -> AsyncIterator[FeatureDTO]:
        ...

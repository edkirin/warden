from typing import AsyncIterator, Optional

from service.api.admin.schema import FeatureDTO
from service.api.common.controller_base import ControllerBase
from service.dto.models import RoleDTO
from service.orm import (
    FeatureActionModel,
    RolePermissionModel,
    UserModel,
    UserPermissionModel,
)
from service.orm.feature import FeatureModel
from service.orm.role import RoleModel


class ReadFeatures(ControllerBase):
    async def execute(
        self, parent_id: Optional[int] = None
    ) -> AsyncIterator[FeatureDTO]:
        async with self.async_session() as session:
            features = FeatureModel.read_all(session, parent_id=parent_id)
            async for feature in features:
                yield FeatureDTO.from_orm(feature)


class ReadRoles(ControllerBase):
    async def execute(self) -> AsyncIterator[RoleDTO]:
        async with self.async_session() as session:
            roles = RoleModel.read_all(session)
            async for roles in roles:
                yield RoleDTO.from_orm(roles)


class DeleteAllData(ControllerBase):
    async def execute(self) -> None:
        async with self.async_session() as session:
            await UserPermissionModel.delete_all(session)
            await RolePermissionModel.delete_all(session)
            await UserModel.delete_all(session)
            await RoleModel.delete_all(session)
            await FeatureActionModel.delete_all(session)
            await FeatureModel.delete_all(session)

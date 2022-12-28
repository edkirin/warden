from typing import AsyncIterator

from service.api.common.controller_base import ControllerBase
from service.api.common.exceptions import UserNotFoundError
from service.dto.models import UserPermissionDTO
from service.orm import UserModel, RoleModel, RolePermissionModel


# class ReadFeatures(ControllerBase):
#     async def execute(
#         self, parent_id: Optional[int] = None
#     ) -> AsyncIterator[FeatureDTO]:
#         async with self.async_session() as session:
#             features = FeatureModel.read_all(session, parent_id=parent_id)
#             async for feature in features:
#                 yield FeatureDTO.from_orm(feature)


class ReadUserPermissions(ControllerBase):
    async def execute(self, tenant_id: int, user_id: int) -> AsyncIterator[UserPermissionDTO]:
        async with self.async_session() as session:
            user = await UserModel.get_by_user_id(session, tenant_id=tenant_id, user_id=user_id)
            if user is None:
                raise UserNotFoundError(tenant_id=tenant_id, user_id=user_id)
            if user.role_id is not None:
                role_permissions = RolePermissionModel.read_for_role_id(session, role_id=user.role_id)
                async for role_permission in role_permissions:
                    print("role_permission:", role_permission.id)

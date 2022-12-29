from typing import Dict, List

from service.api.common.controller_base import ControllerBase
from service.api.common.exceptions import UserNotFoundError
from service.dto.models import UserPermissionActionDTO, UserPermissionDTO
from service.orm import RolePermissionModel, UserModel


PermissionsDict = Dict[str, List[UserPermissionActionDTO]]


class ReadUserPermissions(ControllerBase):
    async def execute(self, tenant_id: int, external_user_id: int) -> List[UserPermissionDTO]:
        async with self.async_session() as session:
            user = await UserModel.get_by_external_user_id(
                session, tenant_id=tenant_id, external_user_id=external_user_id
            )
            if user is None:
                raise UserNotFoundError(tenant_id=tenant_id, external_user_id=external_user_id)

            permissions_dict: PermissionsDict = {}

            if user.role_id is not None:
                role_permissions = RolePermissionModel.read_for_role_id(
                    session, role_id=user.role_id
                )

                async for role_permission in role_permissions:
                    field_name = role_permission.feature.field_name
                    action_dto = UserPermissionActionDTO.from_orm(role_permission)
                    if field_name in permissions_dict:
                        permissions_dict[field_name].append(action_dto)
                    else:
                        permissions_dict[field_name] = [action_dto]

            permissions = [
                UserPermissionDTO(
                    name=name,
                    actions=actions,
                )
                for name, actions in permissions_dict.items()
            ]

            return permissions

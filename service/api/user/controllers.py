from typing import Protocol

from service.api.common.controller_base import ControllerBase
from service.api.common.exceptions import UserNotFoundError
from service.api.enums import ActionEnum
from service.dto.models import UserPermissionDict
from service.orm import RolePermissionModel, UserModel, UserPermissionModel


class PermissionActionProtocol(Protocol):
    action: ActionEnum
    permitted: bool


def _update_permission(
    permissions: UserPermissionDict,
    field_name: str,
    permission_action: PermissionActionProtocol,
):
    if field_name in permissions:
        permissions[field_name][permission_action.action] = permission_action.permitted
    else:
        permissions[field_name] = {
            permission_action.action: permission_action.permitted
        }


class ReadUserPermissions(ControllerBase):
    async def execute(
        self, tenant_id: int, external_user_id: int
    ) -> UserPermissionDict:
        async with self.async_session() as session:
            user = await UserModel.get_by_external_user_id(
                session, tenant_id=tenant_id, external_user_id=external_user_id
            )
            if user is None:
                raise UserNotFoundError(
                    tenant_id=tenant_id, external_user_id=external_user_id
                )

            permissions: UserPermissionDict = {}

            if user.role_id is not None:
                role_permissions = RolePermissionModel.read_for_role_id(
                    session, role_id=user.role_id
                )

                async for role_permission in role_permissions:
                    _update_permission(
                        permissions=permissions,
                        field_name=role_permission.feature.field_name,
                        permission_action=role_permission,
                    )

            user_permissions = UserPermissionModel.read_for_user_id(
                session, user_id=user.id
            )
            async for user_permission in user_permissions:
                _update_permission(
                    permissions=permissions,
                    field_name=user_permission.feature.field_name,
                    permission_action=user_permission,
                )

            return permissions

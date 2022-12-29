from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel

from service.api.enums import ActionEnum


class BaseDTO(BaseModel):
    class Config:
        orm_mode = True


class FeatureDTO(BaseDTO):
    id: int
    name: str
    field_name: str
    parent: Optional[FeatureDTO]


class RoleDTO(BaseDTO):
    id: int
    name: str


class PermissionActionDTO(BaseDTO):
    action: ActionEnum
    permitted: bool


class UserPermissionDTO(BaseDTO):
    name: str
    actions: List[PermissionActionDTO]


UserPermissionDict = Dict[str, Dict[ActionEnum, bool]]


class UserPermissionsDTO(BaseDTO):
    permissions: List[UserPermissionDTO]

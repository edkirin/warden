from enum import Enum


class Role:
    id: int
    name: str


class User:
    tenant_id: int
    user_id: int
    role: Role


class ActionEnum(Enum):
    VIEW = "VIEW"
    CREATE = "CREATE"
    EDIT = "EDIT"
    DELETE = "DELETE"


class FeatureGroup:
    name: str


class Feature:
    name: str
    feature_group: FeatureGroup


class RolePermission:
    role: Role
    feature: Feature
    action: ActionEnum
    permitted: bool


class UserPermission:
    user: User
    feature: Feature
    action: ActionEnum
    permitted: bool

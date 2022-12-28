import factory

from service.api.enums import ActionEnum
from service.factories.base import BaseFactory, get_sequence
from service.orm import FeatureModel, RoleModel, RolePermissionModel

from . import RoleFactory
from .feature import FeatureFactory


class RolePermissionFactory(BaseFactory):
    id: int = get_sequence()
    role: RoleModel = factory.SubFactory(RoleFactory)
    feature: FeatureModel = factory.SubFactory(FeatureFactory)
    action: ActionEnum = ActionEnum.VIEW
    permitted: bool = False

    class Meta:
        model = RolePermissionModel

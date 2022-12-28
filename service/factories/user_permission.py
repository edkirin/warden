import factory

from service.api.enums import ActionEnum
from service.factories.base import BaseFactory, get_sequence
from service.orm import FeatureModel, UserPermissionModel

from .feature import FeatureFactory


class UserPermissionFactory(BaseFactory):
    id: int = get_sequence()
    feature: FeatureModel = factory.SubFactory(FeatureFactory)
    action: ActionEnum = ActionEnum.VIEW
    permitted: bool = False

    class Meta:
        model = UserPermissionModel

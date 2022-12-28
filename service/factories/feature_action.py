import factory

from service.factories.base import BaseFactory, get_sequence
from service.orm import FeatureActionModel, FeatureModel
from .feature import FeatureFactory


class FeatureActionFactory(BaseFactory):
    id: int = get_sequence()
    feature: FeatureModel = factory.SubFactory(FeatureFactory)

    class Meta:
        model = FeatureActionModel

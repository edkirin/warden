import factory

from service.factories.base import BaseFactory, get_sequence
from service.orm import FeatureModel
from .feature_group import FeatureGroupFactory


class FeatureFactory(BaseFactory):
    id = get_sequence()
    name = factory.Faker("pystr", max_chars=30)
    field_name = factory.Faker("pystr", max_chars=30)
    feature_group = factory.SubFactory(FeatureGroupFactory)

    class Meta:
        model = FeatureModel

import factory

from service.factories.base import BaseFactory, get_sequence
from service.orm import FeatureModel


class FeatureFactory(BaseFactory):
    id = get_sequence()
    parent = None
    name = factory.Faker("pystr", max_chars=30)
    field_name = factory.Faker("pystr", max_chars=30)

    class Meta:
        model = FeatureModel

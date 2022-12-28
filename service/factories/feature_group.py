import factory

from service.factories.base import BaseFactory, get_sequence
from service.orm import FeatureGroupModel


class FeatureGroupFactory(BaseFactory):
    id = get_sequence()
    name = factory.Faker("pystr", max_chars=30)
    field_name = factory.Faker("pystr", max_chars=30)

    class Meta:
        model = FeatureGroupModel

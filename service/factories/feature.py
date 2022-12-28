import factory

from service.factories.base import BaseFactory, get_sequence
from service.orm import FeatureModel


class FeatureFactory(BaseFactory):
    id = get_sequence()
    parent = None
    name = factory.Faker("pystr", max_chars=30)
    field_name = factory.LazyAttribute(lambda a: FeatureFactory.create_field_name(a))

    class Meta:
        model = FeatureModel

    @staticmethod
    def create_field_name(instance: FeatureModel) -> str:
        def normalize_name(s: str) -> str:
            return s.lower().replace(" ", "_")

        names = []
        if instance.parent is not None:
            names.append(normalize_name(instance.parent.name))

        names.append(normalize_name(instance.name))

        return ".".join(names)

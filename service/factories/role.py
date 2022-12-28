import factory

from service.factories.base import BaseFactory, get_sequence
from service.orm.role import RoleModel


class RoleFactory(BaseFactory):
    id = get_sequence()
    name = factory.Faker("pystr", max_chars=30)

    class Meta:
        model = RoleModel

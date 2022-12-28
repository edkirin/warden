from typing import Optional

import factory

from service.factories.base import BaseFactory, get_sequence
from service.orm import RoleModel, UserModel


class UserFactory(BaseFactory):
    id: int = get_sequence()
    tenant_id: int = factory.Faker("pyint")
    user_id: int = factory.Faker("pyint")
    role: Optional[RoleModel] = None

    class Meta:
        model = UserModel

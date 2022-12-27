from dataclasses import field, dataclass
from typing import Optional
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
@dataclass
class FeatureGroupModel:
    __table__ = Table(
        "feature_groups",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
        Column("field_name", String),
    )

    id: int = field(init=False)
    name: str
    field_name: str

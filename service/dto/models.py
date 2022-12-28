from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class BaseDTO(BaseModel):
    class Config:
        orm_mode = True


class FeatureDTO(BaseDTO):
    id: int
    name: str
    field_name: str
    parent: Optional[FeatureDTO]


class RoleDTO(BaseDTO):
    id: int
    name: str

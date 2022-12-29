from pydantic import BaseModel

from service.dto.models import FeatureDTO, RoleDTO


class GetFeaturesResponse(BaseModel):
    features: list[FeatureDTO]


class GetRolesResponse(BaseModel):
    roles: list[RoleDTO]

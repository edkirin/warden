from typing import List

from pydantic import BaseModel

from service.dto.models import FeatureDTO, UserPermissionDTO


class GetUserFeaturesResponse(BaseModel):
    features: list[FeatureDTO]


class GetUserPermissionsResponse(BaseModel):
    permissions: List[UserPermissionDTO]

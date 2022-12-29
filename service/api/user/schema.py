from pydantic import BaseModel

from service.dto.models import FeatureDTO, UserPermissionDict


class GetUserFeaturesResponse(BaseModel):
    features: list[FeatureDTO]


# class GetUserPermissionsResponse(BaseModel):
#     permissions: List[UserPermissionDTO]


class GetUserPermissionsResponse(BaseModel):
    permissions: UserPermissionDict

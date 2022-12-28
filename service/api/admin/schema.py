from pydantic import BaseModel

from service.dto.models import FeatureGroupDTO, FeatureDTO


class GetFeatureGroupsResponse(BaseModel):
    feature_groups: list[FeatureGroupDTO]


class GetFeatureGroupsFeaturesResponse(BaseModel):
    features: list[FeatureDTO]

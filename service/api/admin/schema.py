from pydantic import BaseModel

from service.dto.models import FeatureDTO


class GetFeaturesResponse(BaseModel):
    features: list[FeatureDTO]

from pydantic import BaseModel


class BaseDTO(BaseModel):
    class Config:
        orm_mode = True


class FeatureGroupDTO(BaseDTO):
    id: int
    name: str
    field_name: str


class FeatureDTO(BaseDTO):
    id: int
    name: str
    field_name: str
    feature_group: FeatureGroupDTO


class GetFeatureGroupsResponse(BaseModel):
    feature_groups: list[FeatureGroupDTO]


class GetFeatureGroupsFeaturesResponse(BaseModel):
    features: list[FeatureDTO]

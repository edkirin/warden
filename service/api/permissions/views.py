from typing import List
from fastapi import APIRouter
from fastapi import Depends
from service.api.permissions.schema import (
    GetFeatureGroupsFeaturesResponse,
    GetFeatureGroupsResponse,
)
from service.api.permissions.use_cases import (
    ReadAllFeatureGroups,
    ReadFeatureGroupFeatures,
)


router = APIRouter()


@router.get(
    "/feature-groups",
    response_model=GetFeatureGroupsResponse,
)
async def get_feature_groups(
    use_case: ReadAllFeatureGroups = Depends(ReadAllFeatureGroups),
):
    feature_groups = use_case.execute()
    return GetFeatureGroupsResponse(
        feature_groups=[feature_group async for feature_group in feature_groups],
    )


@router.get(
    "/feature-groups/{feature_group_id}/features",
    response_model=GetFeatureGroupsFeaturesResponse,
)
async def get_feature_group_features(
    feature_group_id: int,
    use_case: ReadFeatureGroupFeatures = Depends(ReadFeatureGroupFeatures),
):
    features = use_case.execute(feature_group_id=feature_group_id)
    return GetFeatureGroupsFeaturesResponse(
        features=[feature async for feature in features],
    )


# @router.get(
#     "/tenant/{tenant_id}/permissions/user/{user_id}",
#     response_model=List[FeatureGroupModel],
# )
# async def permissions(tenant_id: int, user_id: int, session: Session = Depends(get_db)):
#     manager = PermissionsManager(session)
#     groups = await manager.get_feature_groups()

#     groups_response = [FeatureGroupDTO.from_orm(group) for group in groups]

#     return groups_response

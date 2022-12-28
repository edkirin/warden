from fastapi import APIRouter
from fastapi import Depends
from service.api.admin.schema import (
    GetFeatureGroupsFeaturesResponse,
    GetFeatureGroupsResponse,
)
from service.api.admin.controllers import (
    ReadAllFeatureGroups,
    ReadFeatureGroupFeatures,
)


router = APIRouter()


@router.get(
    "/feature-groups",
    response_model=GetFeatureGroupsResponse,
)
async def get_feature_groups(
    controller: ReadAllFeatureGroups = Depends(ReadAllFeatureGroups),
):
    feature_groups = controller.execute()
    return GetFeatureGroupsResponse(
        feature_groups=[feature_group async for feature_group in feature_groups],
    )


@router.get(
    "/feature-groups/{feature_group_id}/features",
    response_model=GetFeatureGroupsFeaturesResponse,
)
async def get_feature_group_features(
    feature_group_id: int,
    controller: ReadFeatureGroupFeatures = Depends(ReadFeatureGroupFeatures),
):
    features = controller.execute(feature_group_id=feature_group_id)
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

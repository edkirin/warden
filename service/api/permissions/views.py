from typing import List
from fastapi import APIRouter
from fastapi import Depends
from service.api.permissions.schema import GetFeatureGroupsResponse
from service.api.permissions.use_cases import ReadAllFeatureGroups


router = APIRouter()


@router.get(
    "/feature-groups",
    response_model=GetFeatureGroupsResponse,
)
async def get_feature_groups(
    use_case: ReadAllFeatureGroups = Depends(ReadAllFeatureGroups),
):
    return GetFeatureGroupsResponse(
        feature_groups=[c async for c in use_case.execute()],
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

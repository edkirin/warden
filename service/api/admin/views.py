from fastapi import APIRouter, Depends

from service.api.admin.controllers import DeleteAllData, ReadFeatures, ReadRoles
from service.api.admin.schema import GetFeaturesResponse, GetRolesResponse
from service.factories.create_default_data import create_default_data

router = APIRouter()


@router.get(
    "/admin/features",
    response_model=GetFeaturesResponse,
)
async def get_feature_group_features(
    controller: ReadFeatures = Depends(ReadFeatures),
):
    features = controller.execute()
    return GetFeaturesResponse(
        features=[feature async for feature in features],
    )


@router.get(
    "/admin/roles",
    response_model=GetRolesResponse,
)
async def get_feature_group_features(
    controller: ReadRoles = Depends(ReadRoles),
):
    roles = controller.execute()
    return GetRolesResponse(
        roles=[role async for role in roles],
    )


@router.post("/admin/initial")
async def create_initial_data(
    delete_all_data_controller: DeleteAllData = Depends(DeleteAllData),
):
    await delete_all_data_controller.execute()

    create_default_data()
    return {}


@router.delete("/admin/delete-all")
async def delete_all_data(
    controller: DeleteAllData = Depends(DeleteAllData),
):
    await controller.execute()
    return {}

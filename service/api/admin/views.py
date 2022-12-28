from fastapi import APIRouter, Depends

from service.api.admin.controllers import DeleteAllData, ReadFeatures
from service.api.admin.schema import GetFeaturesResponse
from service.factories.create_default_data import create_default_data

router = APIRouter()


@router.get(
    "/features",
    response_model=GetFeaturesResponse,
)
async def get_feature_group_features(
    controller: ReadFeatures = Depends(ReadFeatures),
):
    features = controller.execute()
    return GetFeaturesResponse(
        features=[feature async for feature in features],
    )


@router.post("/initial")
async def create_initial_data(
    delete_all_data_controller: DeleteAllData = Depends(DeleteAllData),
):
    await delete_all_data_controller.execute()

    create_default_data()
    return {}


@router.delete("/initial")
async def delete_all_data(
    controller: DeleteAllData = Depends(DeleteAllData),
):
    await controller.execute()
    return {}

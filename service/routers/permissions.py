from typing import List
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from service.dependencies import get_db
from service.managers.permissions import PermissionsManager
from service.orm.feature_group import FeatureGroupModel
from service.schemas.feature_group import FeatureGroupDTO


router = APIRouter()


@router.get(
    "/feature-groups",
    response_model=List[FeatureGroupDTO],
)
async def get_feature_groups(db: Session = Depends(get_db)):
    manager = PermissionsManager(db)
    groups = await manager.get_feature_groups()

    return groups


@router.get(
    "/tenant/{tenant_id}/permissions/user/{user_id}",
    response_model=List[FeatureGroupModel],
)
async def permissions(tenant_id: int, user_id: int, db: Session = Depends(get_db)):
    manager = PermissionsManager(db)
    groups = await manager.get_feature_groups()

    groups_response = [FeatureGroupDTO.from_orm(group) for group in groups]

    return groups_response

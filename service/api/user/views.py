from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from service.api.common.exceptions import UserNotFoundError
from service.api.user.controllers import ReadUserPermissions
from service.api.user.schema import GetUserPermissionsResponse

router = APIRouter()


@router.get(
    "/tenant/{tenant_id}/user/{external_user_id}/permissions",
    response_model=GetUserPermissionsResponse,
)
async def get_user_permissions(
    tenant_id: int,
    external_user_id: int,
    controller: ReadUserPermissions = Depends(ReadUserPermissions),
) -> GetUserPermissionsResponse:
    try:
        permissions = await controller.execute(
            tenant_id=tenant_id, external_user_id=external_user_id
        )
    except UserNotFoundError as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ex))

    return GetUserPermissionsResponse(
        permissions=permissions,
    )

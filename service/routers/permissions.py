from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from service.dependencies import get_db


router = APIRouter()


@router.get("/permissions/tenant/{tenant_id}/user/{user_id}")
async def permissions(tenant_id: int, user_id: int, db: Session = Depends(get_db)):
    return {
        "bla": "tra",
        "tenant_id": tenant_id,
        "user_id": user_id,
    }

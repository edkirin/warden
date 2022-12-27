from fastapi import APIRouter
from service.schemas.response import PingSchema


router = APIRouter()


@router.get("/ping", response_model=PingSchema)
async def ping():
    response = PingSchema(result="PONG from warden service!")
    return response

from fastapi import FastAPI

# from service.database import engine, Base
from service.routers import ping
from service.api.permissions.views import router as permissions_router


app = FastAPI()
app.include_router(ping.router)
app.include_router(permissions_router)

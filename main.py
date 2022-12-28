from fastapi import FastAPI

from service.routers import ping
from service.api.admin.views import router as admin_router

app = FastAPI()
app.include_router(ping.router)
app.include_router(admin_router)

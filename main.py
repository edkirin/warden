from fastapi import FastAPI

from service.api.admin.views import router as admin_router
from service.api.user.views import router as user_router
from service.routers import ping

app = FastAPI()
app.include_router(ping.router)
app.include_router(admin_router)
app.include_router(user_router)

"""
test test test
"""

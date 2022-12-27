from fastapi import FastAPI
from service.database import engine, Base
from service.routers import ping
from service.routers import permissions


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(ping.router)
app.include_router(permissions.router)

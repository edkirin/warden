from fastapi import FastAPI

from service.routers import ping
from service.api.admin.views import router as admin_router

app = FastAPI()
app.include_router(ping.router)
app.include_router(admin_router)


from service.factories import FeatureGroupFactory
from service.orm import FeatureGroupModel

FeatureGroupFactory.create(name="bla1", field_name="tra1")
FeatureGroupFactory.create(name="bla2", field_name="tra2")
FeatureGroupFactory.create(name="bla3", field_name="tra3")

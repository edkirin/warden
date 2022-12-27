from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from service.database import Base


class FeatureORM(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    counter = Column(Integer)

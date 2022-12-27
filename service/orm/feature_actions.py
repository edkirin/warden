from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from service.database import Base


class FeatureActionORM(Base):
    __tablename__ = "feature_actions"

    id = Column(Integer, primary_key=True, index=True)
    counter = Column(Integer)

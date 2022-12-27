from typing import List, Type
from sqlalchemy.orm import Session, Query

from service.orm.feature_group import FeatureGroupModel


class PermissionsManager:
    def __init__(self, db: Session):
        self.db = db

    async def get_feature_groups(self) -> List[FeatureGroupModel]:

        query = self.db.query(FeatureGroupModel).order_by(FeatureGroupModel.name)

        return list(query)

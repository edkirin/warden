from pydantic import BaseModel


class FeatureGroupDTO(BaseModel):
    id: int
    name: str
    field_name: str

    class Config:
        orm_mode = True

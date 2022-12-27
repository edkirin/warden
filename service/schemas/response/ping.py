from pydantic import BaseModel


class PingSchema(BaseModel):
    result: str

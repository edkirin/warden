from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from service.database import get_session


class ControllerBase:
    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        self.async_session = session

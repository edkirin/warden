from fastapi import Depends

from service.database import get_session, AsyncSessionClass


class ControllerBase:
    def __init__(self, session: AsyncSessionClass = Depends(get_session)) -> None:
        self.async_session = session

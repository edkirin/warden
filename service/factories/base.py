import factory
from sqlalchemy import orm, create_engine
from sqlalchemy.orm import sessionmaker

from service.config import settings


USE_FACTORY_SEQUENCE = False


def get_sequence():
    if USE_FACTORY_SEQUENCE:
        return factory.Sequence(lambda n: n + 1)
    return None


SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# Session = orm.scoped_session(orm.sessionmaker())
Session = orm.scoped_session(SessionLocal)

class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        # sqlalchemy_session_persistence = factory.alchemy.SESSION_PERSISTENCE_COMMIT
        sqlalchemy_session_persistence = "commit"
        # strategy = factory.enums.BUILD_STRATEGY
        sqlalchemy_session = Session

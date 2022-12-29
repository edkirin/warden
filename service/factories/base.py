import factory
from sqlalchemy import create_engine, orm
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from service.config import settings

USE_FACTORY_SEQUENCE = False


def get_sequence():
    if USE_FACTORY_SEQUENCE:
        return factory.Sequence(lambda n: n + 1)
    return None


db_connect_url = URL.create(
    drivername="postgresql",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)

engine = create_engine(url=db_connect_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Session = orm.scoped_session(SessionLocal)


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        # sqlalchemy_session_persistence = factory.alchemy.SESSION_PERSISTENCE_COMMIT
        sqlalchemy_session_persistence = "commit"
        # strategy = factory.enums.BUILD_STRATEGY
        sqlalchemy_session = Session

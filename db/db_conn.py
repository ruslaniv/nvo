import os
from typing import Optional, Callable

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
# noinspection PyUnresolvedReferences
from sqlalchemy.orm import Session

from db.modelbase import SqlAlchemyBase

from dotenv import load_dotenv
load_dotenv()

db_conf: dict = {
  "user": os.environ.get("POSTGRES_USER"),
  "password": os.environ.get("POSTGRES_PASSWORD"),
  "database": os.environ.get("POSTGRES_DB"),
  "host": os.environ.get("POSTGRES_HOST"),
  "port": os.environ.get("POSTGRES_PORT"),
}

__factory: Optional[Callable[[], Session]] = None
__async_engine: Optional[AsyncEngine] = None


def do_global_init():
    global __factory, __async_engine
    if __factory:
        return
    sync_conn_str = f'postgresql+psycopg2://{db_conf["user"]}:{db_conf["password"]}@{db_conf["host"]}:{db_conf["port"]}/{db_conf["database"]}'
    async_conn_str = f'postgresql+asyncpg://{db_conf["user"]}:{db_conf["password"]}@{db_conf["host"]}:{db_conf["port"]}/{db_conf["database"]}'
    engine = sa.create_engine(sync_conn_str, echo=False)
    __async_engine = create_async_engine(async_conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)
    # noinspection PyUnresolvedReferences
    import db.__all_models__
    # SqlAlchemyBase.metadata.drop_all(engine) # uncommenting this line WILL DROP ALL TABLES IN THE DATABASE!!!!
    SqlAlchemyBase.metadata.create_all(engine)


def create_sync_sa_session() -> Session:
    global __factory
    session: Session = __factory()
    session.expire_on_commit = False
    return session


def get_async_sa_session() -> AsyncSession:
    global __async_engine
    session: AsyncSession = AsyncSession(__async_engine)
    session.sync_session.expire_on_commit = False
    return session

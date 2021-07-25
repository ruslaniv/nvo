from datetime import date
import sqlalchemy as sa
from sqlalchemy import func

from db.modelbase import SqlAlchemyBase


class Message(SqlAlchemyBase):
    __tablename__ = 'messages'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    transport: str = sa.Column(sa.String, index=True)
    target: str = sa.Column(sa.String, index=True)
    message: str = sa.Column(sa.Text)
    created_date: date = sa.Column(sa.TIMESTAMP, default=func.now(), server_default=func.now(), index=True)

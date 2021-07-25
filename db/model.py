import sqlalchemy as sa

from db.modelbase import SqlAlchemyBase


class Message(SqlAlchemyBase):
    __tablename__ = 'messages'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    transport: str = sa.Column(sa.String, index=True)
    target: str = sa.Column(sa.String, index=True)
    message: str = sa.Column(sa.Text)
    created_date: float = sa.Column(sa.Float, index=True)

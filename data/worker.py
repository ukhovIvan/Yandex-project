import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Worker(SqlAlchemyBase):
    __tablename__ = 'Workers'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    position = sa.Column(sa.String)
    number_phone = sa.Column(sa.String)
    email = sa.Column(sa.String)
    password = sa.Column(sa.String)
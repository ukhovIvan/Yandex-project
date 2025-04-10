import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Worker(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'Workers'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    number_phone = sa.Column(sa.String)
    email = sa.Column(sa.String)
    pm_code = sa.Column(sa.String)
    permissions = sa.Column(sa.Integer)
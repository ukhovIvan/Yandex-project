import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Type(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'Type'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    unit = sa.Column(sa.String)

    consumable = orm.relationship('Consumable', back_populates='type')
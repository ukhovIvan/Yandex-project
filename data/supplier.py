import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Supplier(SqlAlchemyBase):
    __tablename__ = 'Suppliers'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    description = sa.Column(sa.String, nullable=True)
    consumable_id = sa.Column(sa.Integer, sa.ForeignKey('Consumables.id'))
    price = sa.Column(sa.Integer, nullable=True)
    count = sa.Column(sa.Integer, nullable=True)

    consumable = orm.relationship('Consumable')
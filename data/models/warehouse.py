import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Warehouse(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'Warehouses'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    address = sa.Column(sa.String)

    consumable_correlation = orm.relationship('WarehouseConsumableCorrelation', back_populates='warehouse')
    delivery_departure = orm.relationship('Delivery', back_populates='warehouse_departure')

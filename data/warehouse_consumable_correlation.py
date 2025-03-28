import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class WarehouseConsumableCorrelation(SqlAlchemyBase):
    __tablename__ = 'WarehouseConsumableCorrelations'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    warehouse_id = sa.Column(sa.Integer, sa.ForeignKey('Warehouses.id'))
    consumable_id = sa.Column(sa.Integer, sa.ForeignKey('Consumables.id'))
    count = sa.Column(sa.Integer, nullable=True)

    warehouse = orm.relationship('Warehouse')
    consumable = orm.relationship('Consumable')
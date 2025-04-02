import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Consumable(SqlAlchemyBase):
    __tablename__ = 'Consumables'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    type_id = sa.Column(sa.Integer, sa.ForeignKey('Type.id'))

    type = orm.relationship('Type')
    warehouse_correlation = orm.relationship('WarehouseConsumableCorrelation', back_populates='consumable')
    catalog_position = orm.relationship('Catalog', back_populates='consumable')
    culture_correlation = orm.relationship('CultureConsumableCorrelation', back_populates='consumable')
    delivery = orm.relationship('Delivery', back_populates='consumable')

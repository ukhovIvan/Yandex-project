import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Catalog(SqlAlchemyBase):
    __tablename__ = 'Catalog'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    consumable_id = sa.Column(sa.Integer, sa.ForeignKey('Consumables.id'))
    supplier_id = sa.Column(sa.Integer, sa.ForeignKey('Suppliers.id'))
    price = sa.Column(sa.Integer)
    comment = sa.Column(sa.String)
    
    consumable = orm.relationship('Consumable')
    supplier = orm.relationship('Suppliers')
    supply = orm.relationship('Supply', back_populates='catalog')

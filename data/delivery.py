import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Delivery(SqlAlchemyBase):
    __tablename__ = 'Deliveries'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    consumable_id = sa.Column(sa.Integer, sa.ForeignKey('Consumables.id'))
    warehouse_departure_id = sa.Column(sa.Integer, sa.ForeignKey('Warehouses.id'))
    warehouse_receive_id = sa.Column(sa.Integer, sa.ForeignKey('Warehouses.id'))
    departure_date = sa.Column(sa.DateTime)
    receive_date = sa.Column(sa.DateTime)
    status = sa.Column(sa.String)
    
    supply = orm.relationship('Supply', back_populates='delivery') 
    warehouse_departure = orm.relationship('Warehouse')
    warehouse_receive = orm.relationship('Warehouse')
    consumable = orm.relationship('Consumable')
    
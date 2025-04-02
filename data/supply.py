import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Supply(SqlAlchemyBase):
    __tablename__ = 'Supplies'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    catalog_id = sa.Column(sa.Integer, sa.ForeignKey('Catalog.id'))
    count = sa.Column(sa.Integer)
    price = sa.Column(sa.Integer)
    order_date = sa.Column(sa.DateTime)
    delivery_date = sa.Column(sa.DateTime)
    delivery_id = sa.Column(sa.Integer, sa.ForeignKey('Deliveries.id'))
    status = sa.Column(sa.String)
    
    delivery = orm.relationship('Delivery')
    catalog = orm.relationship('Catalog')
    
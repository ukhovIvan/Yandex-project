import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Order(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'Orders'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    id_buyer = sa.Column(sa.Integer, sa.ForeignKey('Buyers.id'))
    order_date = sa.Column(sa.DateTime)
    complete_date = sa.Column(sa.DateTime, nullable=True)
    income = sa.Column(sa.Integer)
    expense = sa.Column(sa.Integer)
    profit = sa.Column(sa.Integer)
    status = sa.Column(sa.String)
    
    buyer = orm.relationship('Buyer')
    batch = orm.relationship('Batch', back_populates='order')
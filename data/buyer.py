import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Buyer(SqlAlchemyBase):
    __tablename__ = 'Buyers'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    address = sa.Column(sa.String)
    phone_number = sa.Column(sa.String)
    email = sa.Column(sa.String)
    password = sa.Column(sa.String)

    order = orm.relationship('Order', back_populates='buyer')

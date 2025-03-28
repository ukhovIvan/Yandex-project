import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Buyer(SqlAlchemyBase):
    __tablename__ = 'Buyers'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    address = sa.Column(sa.String)

    batch = orm.relationship('Batch', back_populates='buyer')
    culture_correlation = orm.relationship('CultureBuyerCorrelation', back_populates='buyer')

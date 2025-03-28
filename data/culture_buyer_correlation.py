import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class CultureBuyerCorrelation(SqlAlchemyBase):
    __tablename__ = 'CultureBuyerCorrelations'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    buyer_id = sa.Column(sa.Integer, sa.ForeignKey('Buyers.id'))
    culture_id = sa.Column(sa.Integer, sa.ForeignKey('Cultures.id'))
    sale = sa.Column(sa.Integer)

    buyer = orm.relationship('Buyer')
    culture = orm.relationship('Culture')
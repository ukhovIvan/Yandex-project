import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Batch(SqlAlchemyBase):
    __tablename__ = 'Batches'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    order_id = sa.Column(sa.Integer, sa.ForeignKey('Orders.id'))
    culture_id = sa.Column(sa.Integer, sa.ForeignKey('Cultures.id'))
    count = sa.Column(sa.Integer)
    start_date = sa.Column(sa.DateTime)
    end_date = sa.Column(sa.DateTime)
    status_view = sa.Column(sa.String)
    status_real = sa.Column(sa.String)

    order = orm.relationship('Order', back_populates='batch')
    culture = orm.relationship('Culture', back_populates='batch')

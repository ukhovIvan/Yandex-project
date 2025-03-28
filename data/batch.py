import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Batch(SqlAlchemyBase):
    __tablename__ = 'Batches'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    culture_id = sa.Column(sa.Integer, sa.ForeignKey('Cultures.id'))
    count = sa.Column(sa.Integer)
    start_date = sa.Column(sa.DateTime)
    sale_date = sa.Column(sa.DateTime)
    condition_id = sa.Column(sa.Integer, sa.ForeignKey('Conditions.id'))
    buyer_id = sa.Column(sa.Integer, sa.ForeignKey('Buyers.id'))

    buyer = orm.relationship('Buyer')
    condition = orm.relationship('Condition')
    checklist = orm.relationship('Checklist', back_populates='batch')

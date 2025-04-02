import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Culture(SqlAlchemyBase):
    __tablename__ = 'Cultures'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    instruction = sa.Column(sa.String)

    batch = orm.relationship('Batch', back_populates='culture')
    consumable_correlation = orm.relationship('CultureConsumableCorrelation', back_populates='culture')

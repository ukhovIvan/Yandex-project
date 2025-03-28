import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Condition(SqlAlchemyBase):
    __tablename__ = 'Conditions'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    in_process = sa.Column(sa.Boolean)

    batch = orm.relationship('Batch', back_populates='condition')
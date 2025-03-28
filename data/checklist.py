import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Checklist(SqlAlchemyBase):
    __tablename__ = 'Checklist'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    batch_id = sa.Column(sa.Integer, sa.ForeignKey('Batches.id'))
    stage_1 = sa.Column(sa.Boolean)
    stage_2 = sa.Column(sa.Boolean)
    stage_3 = sa.Column(sa.Boolean)

    batch = orm.relationship('Batch')
import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Expense(SqlAlchemyBase):
    __tablename__ = 'Expenses'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    seed_weight = sa.Column(sa.Integer)
    seed_id = sa.Column(sa.Integer, sa.ForeignKey('Consumables.id'))
    box_id = sa.Column(sa.Integer, sa.ForeignKey('Consumables.id'))
    substrate_id = sa.Column(sa.Integer, sa.ForeignKey('Consumables.id'))

    seed = orm.relationship('Consumable')
    box = orm.relationship('Consumable')
    substrate = orm.relationship('Consumable')
    culture_expense = orm.relationship('Culture', back_populates='expense')

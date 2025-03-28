import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Consumable(SqlAlchemyBase):
    __tablename__ = 'Consumables'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    type_id = sa.Column(sa.Integer, sa.ForeignKey('Type.id'))

    type = orm.relationship('Type')
    warehouse_correlation = orm.relationship('WarehouseConsumableCorrelation', back_populates='consumable')
    supplier = orm.relationship('Supplier', back_populates='consumable')
    seed_expense = orm.relationship('Expense', back_populates='seed')
    box_expense = orm.relationship('Expense', back_populates='box')
    substrate_expense = orm.relationship('Expense', back_populates='substrate')
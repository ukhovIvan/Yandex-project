import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Culture(SqlAlchemyBase):
    __tablename__ = 'Cultures'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    expense_id = sa.Column(sa.Integer, sa.ForeignKey('Expenses.id'))
    stage_1 = sa.Column(sa.String)
    description_1 = sa.Column(sa.String, nullable=True)
    stage_2 = sa.Column(sa.String)
    description_2 = sa.Column(sa.String, nullable=True)
    stage_3  = sa.Column(sa.String)
    description_3 = sa.Column(sa.String, nullable=True)

    expense = orm.relationship('Expense')
    buyer_correlation = orm.relationship('CultureBuyerCorrelation', back_populates='culture')

import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.db_session import SqlAlchemyBase


class Supplier(SqlAlchemyBase):
    __tablename__ = 'Suppliers'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    address = sa.Column(sa.String)

    catalog_position = orm.relationship('Catalog', back_populates='supplier')
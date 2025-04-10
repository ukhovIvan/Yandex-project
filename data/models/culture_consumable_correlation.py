import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class CultureConsumableCorrelation(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'CultureConsumableCorrelations'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    culture_id = sa.Column(sa.Integer, sa.ForeignKey('Cultures.id'))
    consumable_id = sa.Column(sa.Integer, sa.ForeignKey('Consumables.id'))
    count = sa.Column(sa.Integer)

    culture = orm.relationship('Culture')
    consumable = orm.relationship('Consumable')

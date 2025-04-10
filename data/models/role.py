import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin
from .permission import Permission
from data.db_session import *


class Role(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'Roles'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, unique=True)
    default = sa.Column(sa.Boolean, default=False)
    permissions = sa.Column(sa.Integer)

    # users = orm.relationship('User')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm
    '''
    @staticmethod
    def insert_roles():
        global_init(f'db/Roles.sqlite')
        db_sess = create_session()
        roles = {
            'Farmer': [],
            'Warehouse_manager': [],
            'CRM': [],
            'Admin': []
        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db_sess.add(role)
        db_sess.commit()'''




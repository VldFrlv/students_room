from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()

# Способ 1 создания моделей "Императивный"

roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('role', String(20))
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String(50)),
    Column('username', String(50)),
    Column('password', String()),
    Column('name', String(20)),
    Column('surname', String(20)),
    Column('role_id', Integer, ForeignKey('roles.id'))
)

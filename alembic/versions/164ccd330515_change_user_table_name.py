"""Change user table name

Revision ID: 164ccd330515
Revises: 6044286f0a05
Create Date: 2024-02-16 19:18:32.287102

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '164ccd330515'
down_revision: Union[str, None] = '6044286f0a05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('alteryx_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('alteryx_api_key', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('alteryx_api_secret', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('disabled', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###

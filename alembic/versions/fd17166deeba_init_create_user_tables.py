"""init - create user tables

Revision ID: fd17166deeba
Revises: 
Create Date: 2024-02-10 19:33:03.773974

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'fd17166deeba'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('alteryx_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('alteryx_api_key', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('alteryx_api_secret', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###

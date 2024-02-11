"""exend user table columns

Revision ID: 6044286f0a05
Revises: fd17166deeba
Create Date: 2024-02-11 21:57:13.056349

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '6044286f0a05'
down_revision: Union[str, None] = 'fd17166deeba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('users', sa.Column('full_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('users', sa.Column('disabled', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'disabled')
    op.drop_column('users', 'full_name')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###

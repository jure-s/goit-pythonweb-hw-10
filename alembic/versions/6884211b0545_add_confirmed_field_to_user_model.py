"""Add confirmed field to User model

Revision ID: 6884211b0545
Revises: 7a6821247c93
Create Date: 2025-03-16 14:19:09.787477

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6884211b0545'
down_revision: Union[str, None] = '7a6821247c93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###

"""Create User table

Revision ID: 2fa592a307b8
Revises: 
Create Date: 2026-02-18 14:24:55.779293

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2fa592a307b8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "Users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("pass", sa.String(50), nullable=False),
        sa.Column("exist", sa.Boolean, default=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("Users")

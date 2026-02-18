"""add role column

Revision ID: 76c50638b01c
Revises: 2fa592a307b8
Create Date: 2026-02-18 14:46:36.508430

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76c50638b01c'
down_revision: Union[str, Sequence[str], None] = '2fa592a307b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "Users",
        sa.Column("role", sa.String(50), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("Users", "role")

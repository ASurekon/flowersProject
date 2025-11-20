"""empty message

Revision ID: 1b9a1d357b3e
Revises: 0c259ddf8c85
Create Date: 2025-11-20 10:50:26.258602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b9a1d357b3e'
down_revision: Union[str, Sequence[str], None] = '0c259ddf8c85'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

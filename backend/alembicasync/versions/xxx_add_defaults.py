from alembic import op
import sqlalchemy as sa

revision = '123456789abc'
down_revision = '1b9a1d357b3e'

def upgrade():
    # Добавляем колонку с default
    # op.add_column('flowers', 
    #     sa.Column('status', sa.String(20), server_default='active')
    # )

    # Или изменяем существующую колонку
    op.alter_column('flowers', 'available',
        server_default='true'
    )
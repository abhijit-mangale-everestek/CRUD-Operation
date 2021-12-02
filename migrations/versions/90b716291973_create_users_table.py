"""create users table

Revision ID: 90b716291973
Revises: 
Create Date: 2021-11-29 14:55:58.235834

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '90b716291973'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(10), nullable=False),
        sa.Column('last_name', sa.String(10), nullable=False),
        sa.Column('gender', sa.String(10), nullable=False),
    )


def downgrade():
    op.drop_table('users')

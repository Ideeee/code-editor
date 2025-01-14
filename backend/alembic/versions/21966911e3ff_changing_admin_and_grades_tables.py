"""changing admin and grades tables

Revision ID: 21966911e3ff
Revises: 32ab0c0a4912
Create Date: 2023-07-23 16:49:50.012605

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '21966911e3ff'
down_revision = '32ab0c0a4912'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admin', 'last_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('admin', 'username',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('admin', 'role',
               existing_type=postgresql.ENUM('BaseAdmin', 'User', name='role'),
               nullable=False)
    op.create_unique_constraint(None, 'admin', ['username'])
    op.add_column('student', sa.Column('department', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'department')
    op.drop_constraint(None, 'admin', type_='unique')
    op.alter_column('admin', 'role',
               existing_type=postgresql.ENUM('BaseAdmin', 'User', name='role'),
               nullable=True)
    op.alter_column('admin', 'username',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('admin', 'last_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###

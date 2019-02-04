"""empty message

Revision ID: e3c0ed818ace
Revises: 9a873710d0a3
Create Date: 2019-02-04 15:30:05.680703

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e3c0ed818ace'
down_revision = '9a873710d0a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    op.add_column('user', sa.Column('password', sa.String(length=128), nullable=True))
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=True))
    op.drop_column('user', 'password')
    op.drop_constraint(None, 'post', type_='foreignkey')
    # ### end Alembic commands ###

"""Final migration

Revision ID: ca9a412d35a2
Revises: 
Create Date: 2023-11-29 10:05:52.367025

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ca9a412d35a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_column('updated_at')

    with op.batch_alter_table('session', schema=None) as batch_op:
        batch_op.add_column(sa.Column('session_token', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('logout_timestamp', sa.DateTime(), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activation_code', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('activation_code')

    with op.batch_alter_table('session', schema=None) as batch_op:
        batch_op.drop_column('logout_timestamp')
        batch_op.drop_column('session_token')

    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', mysql.DATETIME(), nullable=True))

    # ### end Alembic commands ###

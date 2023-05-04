"""Adding user is_verify option

Revision ID: 51dd9097baaa
Revises: f248b8085bf8
Create Date: 2023-05-03 09:57:13.268664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51dd9097baaa'
down_revision = 'f248b8085bf8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_verify', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_verify')

    # ### end Alembic commands ###
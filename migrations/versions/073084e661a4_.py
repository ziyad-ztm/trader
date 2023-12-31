"""empty message

Revision ID: 073084e661a4
Revises: 
Create Date: 2023-10-28 17:19:55.611648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '073084e661a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_color', sa.String(length=25), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('profile_color')

    # ### end Alembic commands ###

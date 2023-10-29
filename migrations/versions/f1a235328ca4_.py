"""empty message

Revision ID: f1a235328ca4
Revises: 073084e661a4
Create Date: 2023-10-29 16:21:03.015262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1a235328ca4'
down_revision = '073084e661a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['received_by'], ['id'])
        batch_op.create_foreign_key(None, 'user', ['sent_by'], ['id'])

    with op.batch_alter_table('favourite_items', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'item', ['item_id'], ['id'])

    with op.batch_alter_table('image', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'item', ['item_id'], ['id'])

    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['owner'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['owner'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('image', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'item', ['item_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('favourite_items', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'item', ['item_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['sent_by'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'user', ['received_by'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###

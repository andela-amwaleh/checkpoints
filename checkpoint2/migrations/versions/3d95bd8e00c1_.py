"""empty message

Revision ID: 3d95bd8e00c1
Revises: 56715b423ca4
Create Date: 2015-12-05 09:11:31.552466

"""

# revision identifiers, used by Alembic.
revision = '3d95bd8e00c1'
down_revision = '56715b423ca4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bucketitem', sa.Column('done', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bucketitem', 'done')
    ### end Alembic commands ###
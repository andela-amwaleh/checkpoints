"""empty message

Revision ID: 2fc243ea19c8
Revises: 36190af796df
Create Date: 2015-11-28 15:50:40.682275

"""

# revision identifiers, used by Alembic.
revision = '2fc243ea19c8'
down_revision = '36190af796df'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bucketitems', sa.Column('created_on', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True))
    op.drop_column('bucketitems', 'reated_on')
    op.add_column('users', sa.Column('created_on', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True))
    op.add_column('users', sa.Column('modified_on', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'modified_on')
    op.drop_column('users', 'created_on')
    op.add_column('bucketitems', sa.Column('reated_on', postgresql.TIMESTAMP(), server_default=sa.text(u'now()'), autoincrement=False, nullable=True))
    op.drop_column('bucketitems', 'created_on')
    ### end Alembic commands ###
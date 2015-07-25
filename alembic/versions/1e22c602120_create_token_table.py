"""Create token table

Revision ID: 1e22c602120
Revises: 1121962e64a
Create Date: 2015-07-24 13:21:24.193562

"""

# revision identifiers, used by Alembic.
revision = '1e22c602120'
down_revision = '1121962e64a'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token',
    sa.Column('token', sa.Unicode(), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('deleted', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('token')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token')
    ### end Alembic commands ###

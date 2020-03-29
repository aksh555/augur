"""empty message

Revision ID: 12d347e3a09e
Revises: 2ced44bb51b4
Create Date: 2020-03-29 03:32:33.431413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12d347e3a09e'
down_revision = '2ced44bb51b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contributor', sa.Column('repo_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contributor', 'repo_id')
    # ### end Alembic commands ###
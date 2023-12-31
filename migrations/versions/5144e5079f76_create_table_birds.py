"""create table birds

Revision ID: 5144e5079f76
Revises: 
Create Date: 2023-10-31 08:43:08.976737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5144e5079f76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('birds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('birds')
    # ### end Alembic commands ###

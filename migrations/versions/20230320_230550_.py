"""empty message

Revision ID: 4e6cc1b9845e
Revises: ffdc0a98111c
Create Date: 2023-03-20 23:05:50.576379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e6cc1b9845e'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('petTypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pet', sa.String(length=40), nullable=False),
    sa.Column('color', sa.String(length=40), nullable=False),
    sa.Column('maxGrowth', sa.DECIMAL(precision=50, scale=2), nullable=False),
    sa.Column('mainImg', sa.String(length=1000), nullable=False),
    sa.Column('sadImg', sa.String(length=1000), nullable=False),
    sa.Column('madImg', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ownerId', sa.Integer(), nullable=True),
    sa.Column('petTypeId', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('currGrowth', sa.DECIMAL(precision=50, scale=2), nullable=False),
    sa.Column('hunger', sa.DECIMAL(precision=50, scale=2), nullable=False),
    sa.Column('description', sa.String(length=4000), nullable=True),
    sa.ForeignKeyConstraint(['ownerId'], ['users.id'], ),
    sa.ForeignKeyConstraint(['petTypeId'], ['petTypes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    op.drop_table('petTypes')
    # ### end Alembic commands ###
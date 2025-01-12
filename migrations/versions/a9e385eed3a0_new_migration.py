"""new migration

Revision ID: a9e385eed3a0
Revises: 
Create Date: 2024-01-29 16:49:26.181902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9e385eed3a0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=30), nullable=False),
                    sa.Column('description', sa.String(
                        length=200), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('groups',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=5), nullable=False),
                    sa.Column('course_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('students',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('first_name', sa.String(
                        length=20), nullable=False),
                    sa.Column('last_name', sa.String(
                        length=25), nullable=False),
                    sa.Column('group_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    op.drop_table('groups')
    op.drop_table('courses')
    # ### end Alembic commands ###

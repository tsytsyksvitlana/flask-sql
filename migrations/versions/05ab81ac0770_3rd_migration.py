"""3rd migration

Revision ID: 05ab81ac0770
Revises: a6dee405f19b
Create Date: 2023-11-23 19:17:06.281772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05ab81ac0770'
down_revision: Union[str, None] = 'a6dee405f19b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('students_group_id_fkey', 'students', type_='foreignkey')
    op.drop_column('students', 'group_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('students_group_id_fkey', 'students', 'groups', ['group_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###

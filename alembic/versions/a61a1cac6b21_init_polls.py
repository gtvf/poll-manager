"""init

Revision ID: a61a1cac6b21
Revises: 
Create Date: 2021-07-17 23:19:37.199555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a61a1cac6b21'
down_revision = 'a61a1cac6b20'
branch_labels = None
depends_on = 'a61a1cac6b20'


def upgrade():
    op.create_table('polls',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('polls_id_seq'::regclass)"),
                              autoincrement=True, nullable=False),
                    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='polls_user_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='polls_pkey'),
                    postgresql_ignore_search_path=False
                    )
    op.create_index('ix_polls_id', 'polls', ['id'], unique=False)


def downgrade():
    op.drop_index('ix_polls_id', table_name='polls')
    op.drop_table('polls')

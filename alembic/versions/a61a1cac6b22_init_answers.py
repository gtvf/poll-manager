"""init

Revision ID: a61a1cac6b22
Revises: 
Create Date: 2021-07-17 23:19:37.199555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a61a1cac6b22'
down_revision = 'a61a1cac6b21'
branch_labels = None
depends_on = 'a61a1cac6b21'


def upgrade():
    op.create_table('answers',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('answers_id_seq'::regclass)"),
                              autoincrement=True, nullable=False),
                    sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('poll_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['poll_id'], ['polls.id'], name='answers_poll_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='answers_pkey'),
                    postgresql_ignore_search_path=False
                    )
    op.create_index('ix_answers_id', 'answers', ['id'], unique=False)


def downgrade():
    op.drop_index('ix_answers_id', table_name='answers')
    op.drop_table('answers')

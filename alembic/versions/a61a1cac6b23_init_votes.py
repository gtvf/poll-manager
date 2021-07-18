"""init

Revision ID: a61a1cac6b23
Revises: 
Create Date: 2021-07-17 23:19:37.199555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a61a1cac6b23'
down_revision = 'a61a1cac6b22'
branch_labels = None
depends_on = 'a61a1cac6b22'


def upgrade():
    op.create_table('votes',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('poll_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('answer_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['answer_id'], ['answers.id'], name='votes_answer_id_fkey'),
                    sa.ForeignKeyConstraint(['poll_id'], ['polls.id'], name='votes_poll_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='votes_pkey')
                    )
    op.create_index('ix_votes_id', 'votes', ['id'], unique=False)


def downgrade():
    op.drop_index('ix_votes_id', table_name='votes')
    op.drop_table('votes')

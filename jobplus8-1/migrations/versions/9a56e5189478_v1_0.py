"""v1.0

Revision ID: 9a56e5189478
Revises: 
Create Date: 2018-10-29 19:20:53.795289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a56e5189478'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('phonenumber', sa.Text(), nullable=True),
    sa.Column('work_experience', sa.SmallInteger(), nullable=True),
    sa.Column('upload_resume_jobname', sa.String(length=64), nullable=True),
    sa.Column('is_disable', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('company',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=512), nullable=False),
    sa.Column('logo', sa.String(length=512), nullable=True),
    sa.Column('about', sa.String(length=1024), nullable=False),
    sa.Column('description', sa.String(length=24), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.Text(), nullable=True),
    sa.Column('c_email', sa.String(length=24), nullable=False),
    sa.Column('tags', sa.String(length=128), nullable=True),
    sa.Column('stack', sa.String(length=128), nullable=True),
    sa.Column('field', sa.String(length=32), nullable=True),
    sa.Column('financing', sa.String(length=32), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jobname', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('experience_requirement', sa.String(length=32), nullable=True),
    sa.Column('degree_requirement', sa.String(length=32), nullable=True),
    sa.Column('lowest_salary', sa.Integer(), nullable=True),
    sa.Column('highest_salary', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=24), nullable=True),
    sa.Column('education', sa.String(length=32), nullable=True),
    sa.Column('job_label', sa.String(length=128), nullable=True),
    sa.Column('is_fulltime', sa.Boolean(), nullable=True),
    sa.Column('is_open', sa.Boolean(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('delivery',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('response', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_job',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_job')
    op.drop_table('delivery')
    op.drop_table('job')
    op.drop_table('company')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###

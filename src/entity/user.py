import sqlalchemy as sa

from src.entity.base import Base
from src.entity.mixin import TimestampMixin


class User(TimestampMixin, Base):
    email = sa.Column(sa.String(255), nullable=False)
    first_name = sa.Column(sa.String(255), nullable=False)
    last_name = sa.Column(sa.String(255), nullable=False)

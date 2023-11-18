from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from web_app.db.models.base import Base


class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=5), unique=True)

    def __repr__(self):
        return (f'Group(id={self.id}, name={self.name})')

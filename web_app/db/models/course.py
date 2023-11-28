import typing as t
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from web_app.db.models import Base

if t.TYPE_CHECKING:
    from web_app.db.models.group import Group


class Course(Base):
    __tablename__ = 'courses'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=30))
    description: Mapped[str] = mapped_column(String(length=200))
    groups: Mapped['Group'] = relationship(back_populates='course')

    def __repr__(self):
        return (f'Course(id={self.id}, '
                f'name={self.name}, '
                f'description={self.description})')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

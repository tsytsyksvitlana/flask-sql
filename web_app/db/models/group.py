from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer

from web_app.db.models.base import Base


if TYPE_CHECKING:
    from web_app.db.models.course import Course
    from web_app.db.models.student import Student


class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=5))
    students: Mapped[list['Student']] = relationship(
        back_populates='group', lazy='selectin')
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'))
    course: Mapped['Course'] = relationship(
        back_populates='groups', lazy='select')

    def __repr__(self):
        return (f'Group(id={self.id}, name={self.name})')

    def to_dict(self):
        return {
            "name": self.name,
            "student": [s.to_dict() for s in self.students],
            "course": [s.to_dict() for s in self.course]
        }

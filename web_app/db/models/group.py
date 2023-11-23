from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer

from web_app.db.models.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from web_app.db.models.course import Course
    from web_app.db.models.student import Student


class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=5))
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey('students.id'))
    student: Mapped['Student'] = relationship('Student', backref='groups')
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey('courses.id'))
    course: Mapped['Course'] = relationship(
        "Course", back_populates="groups")

    def __repr__(self):
        return (f'Group(id={self.id}, name={self.name})')

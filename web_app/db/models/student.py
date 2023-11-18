from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey

from web_app.db.models.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from web_app.db.models.course import Course
    from web_app.db.models.group import Group


class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int] = mapped_column(
        ForeignKey('groups.id', ondelete='CASCADE'))
    group: Mapped['Group'] = relationship('Group', backref='students')
    first_name: Mapped[str] = mapped_column(String(length=20))
    last_name: Mapped[str] = mapped_column(String(length=25))
    courses: Mapped['Course'] = relationship(
        "courses", back_populates="students")

    def __repr__(self):
        return (f'Student(id={self.id}, '
                f'group_id={self.group_id}, '
                f'first_name={self.first_name}, '
                f'last_name={self.last_name})')

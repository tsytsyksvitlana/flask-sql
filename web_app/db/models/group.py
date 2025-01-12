from typing import TYPE_CHECKING, Any
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

    students: Mapped[list['Student']] = relationship(back_populates='group')

    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'))
    course: Mapped['Course'] = relationship(back_populates='groups')

    def __repr__(self):
        return (f'Group(id={self.id}, name={self.name})')

    def to_dict(self, exclude: set | None = None) -> dict[str, Any]:
        if exclude is None:
            exclude = set()
        data = {
            Group.id.key: self.id,
            Group.name.key: self.name
        }
        if 'course' not in exclude:
            data['course'] = self.course.to_dict(
                exclude={'groups', 'students'})
        if 'students' not in exclude:
            data['students'] = [
                s.to_dict(exclude={'group', 'courses'}) for s in self.students]
        return data

import typing as t
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey

from web_app.db.models.base import Base

if t.TYPE_CHECKING:
    from web_app.db.models.group import Group
    from web_app.db.models.course import Course


class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(length=20))
    last_name: Mapped[str] = mapped_column(String(length=25))
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'))
    group: Mapped['Group'] = relationship(
        back_populates='students', join_depth=1)
    courses: Mapped[list['Course']] = relationship(secondary='groups')

    def __repr__(self):
        return (f'Student(first_name={self.first_name}, '
                f'last_name={self.last_name})')

    def to_dict(self, exclude: set | None = None) -> dict[str, t.Any]:
        if exclude is None:
            exclude = set()
        data = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
        if 'group' not in exclude:
            data['group'] = self.group.to_dict(exclude={'students', 'courses'})
        if 'course' not in exclude:
            data['course'] = [
                c.to_dict(exclude={'students', 'group'}) for c in self.course]
        return data

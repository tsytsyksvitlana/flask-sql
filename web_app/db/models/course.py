import typing as t
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from web_app.db.models import Base

if t.TYPE_CHECKING:
    from web_app.db.models.group import Group
    from web_app.db.models.group import Student


class Course(Base):
    __tablename__ = 'courses'
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(length=30))
    description: Mapped[str] = mapped_column(String(length=200))

    groups: Mapped[list['Group']] = relationship(back_populates='course')
    students: Mapped[list['Student']] = relationship(
        primaryjoin='Course.id == Group.course_id and Group.id == Student.group_id',
        secondary='groups', back_populates='courses', lazy='selectin')

    def __repr__(self):
        return (f'Course(id={self.id}, '
                f'name={self.name}, '
                f'description={self.description})')

    def to_dict(self):
        if exclude is None:
            exclude = set()
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

        if 'groups' not in exclude:
            data['groups'] = [group.to_dict(
                exclude={'course', 'students'}) for group in self.groups]
        if 'students' not in exclude:
            data['students'] = [group.to_dict(
                exclude={'courses', 'groups'}) for group in self.students]
        return data

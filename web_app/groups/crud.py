from sqlalchemy import select, func, Sequence
from sqlalchemy.orm import joinedload

from web_app.db.session import s
from web_app.db.models.group import Group
from web_app.db.models.student import Student


def get_groups(
        course_id: int | None,
        student_id: int | None,
        count_students: int | None,
) -> Sequence[Group]:
    query = (
        select(Group).options(
            joinedload(Group.course),
            joinedload(Group.students))
    )
    if course_id:
        query = query.where(Group.course_id == course_id)
    if student_id:
        query = query.where(Group.students.any(Student.id == student_id))
    if count_students:
        query = query.having(func.count(Group.name) <= count_students)
        query = query.group_by(Group.id, Student.id)
    return s.users_db.scalars(query).all()


def get_group(group_id: int) -> Group | None:
    query = (
        select(Group)
        .options(
            joinedload(Group.id),
            joinedload(Group.students)
        )
        .where(Group.id == group_id)
    )
    groups = s.users_db.scalar(query)
    return groups
